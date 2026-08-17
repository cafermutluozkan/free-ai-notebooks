"""ARDY Motion Generator — Hugging Face Space (TheBuildAI edition).

Runs NVIDIA ARDY (SIGGRAPH 2026, https://github.com/nv-tlabs/ardy) text-to-motion
inference on ZeroGPU (or any GPU hardware tier the Space is assigned) and renders
a lightweight joint-scatter preview video plus the raw .npz motion data.

`import spaces` must happen before any CUDA-touching import (torch, etc.) so the
ZeroGPU runtime can patch CUDA initialization correctly.
"""

import spaces  # noqa: E402  (must be imported first, see module docstring)

import os
import subprocess
import sys
import uuid
from pathlib import Path

import gradio as gr
import numpy as np

APP_DIR = Path(__file__).resolve().parent
REPO_DIR = APP_DIR / "ardy_repo"
OUTPUT_DIR = REPO_DIR / "outputs"
ARDY_GIT_URL = "https://github.com/nv-tlabs/ardy.git"
LLAMA_REPO = "meta-llama/Meta-Llama-3-8B-Instruct"


def ensure_ardy_installed() -> None:
    """Clone NVIDIA ARDY and install it (core inference only) if missing."""
    if not (REPO_DIR / "scripts" / "generate.py").exists():
        print(f"Cloning ARDY into {REPO_DIR} ...")
        subprocess.run(
            ["git", "clone", "--depth", "1", ARDY_GIT_URL, str(REPO_DIR)],
            check=True,
        )

    try:
        import importlib

        importlib.import_module("ardy")
        print("ardy package already importable.")
    except ImportError:
        print("Installing ARDY (core inference only)...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-e", "."],
            cwd=REPO_DIR,
            check=True,
        )

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


def apply_fp16_compat_patch() -> None:
    """Let LLM2Vec run in FP16 on pre-Ampere GPUs (e.g. T4) that lack native BF16.

    This is idempotent and a no-op if the Space's GPU already supports BF16
    natively (Ampere/Hopper, which is what ZeroGPU typically provides).
    """
    load_model_file = REPO_DIR / "ardy" / "model" / "load_model.py"
    if not load_model_file.exists():
        return

    source = load_model_file.read_text(encoding="utf-8")
    old = (
        "    dtype = torch.float32 if fp32 else torch.bfloat16\n"
        "    return text_encoder.to(device=device, dtype=dtype)"
    )
    new = (
        "    if fp32:\n"
        "        dtype = torch.float32\n"
        "    elif str(device).startswith(\"cuda\") and torch.cuda.get_device_capability(device)[0] < 8:\n"
        "        dtype = torch.float16\n"
        "    else:\n"
        "        dtype = torch.bfloat16\n"
        "    return text_encoder.to(device=device, dtype=dtype)"
    )
    if new in source or old not in source:
        return
    load_model_file.write_text(source.replace(old, new, 1), encoding="utf-8")
    print("Applied FP16 compatibility patch to ardy/model/load_model.py")


def render_skeleton_video(joints: np.ndarray, output_path: Path, fps: int = 20) -> None:
    """Render a lightweight 3D joint-scatter animation as an MP4 preview."""
    import matplotlib

    matplotlib.use("Agg")
    import imageio
    import matplotlib.pyplot as plt

    x_min, x_max = float(joints[..., 0].min()), float(joints[..., 0].max())
    y_min, y_max = float(joints[..., 2].min()), float(joints[..., 2].max())
    z_min, z_max = float(joints[..., 1].min()), float(joints[..., 1].max())

    writer = imageio.get_writer(str(output_path), fps=fps, codec="libx264", quality=8)
    try:
        for frame in joints:
            fig = plt.figure(figsize=(5, 5), dpi=120)
            ax = fig.add_subplot(111, projection="3d")
            ax.scatter(frame[:, 0], frame[:, 2], frame[:, 1], s=25, c="#7c5cff")
            ax.set_xlim(x_min, x_max)
            ax.set_ylim(y_min, y_max)
            ax.set_zlim(z_min, z_max)
            ax.set_axis_off()
            ax.set_box_aspect((1, 1, 1))
            fig.canvas.draw()
            image = np.asarray(fig.canvas.buffer_rgba())[:, :, :3]
            writer.append_data(image)
            plt.close(fig)
    finally:
        writer.close()


ensure_ardy_installed()
apply_fp16_compat_patch()


@spaces.GPU(duration=120)
def generate_motion(prompt, duration_seconds, diffusion_steps, history_frames, seed):
    if not prompt or not prompt.strip():
        raise gr.Error("Please enter a text prompt describing the motion.")

    hf_token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")
    if not hf_token:
        raise gr.Error(
            "This Space is missing an HF_TOKEN secret with approved access to "
            f"{LLAMA_REPO}. Space owner: add it under Settings -> Repository secrets."
        )

    history_frames = int(history_frames)
    if history_frames % 4 != 0 or history_frames <= 0:
        raise gr.Error("History frames must be a positive multiple of 4.")

    run_id = uuid.uuid4().hex[:8]
    output_name = f"space_{run_id}"

    env = os.environ.copy()
    env["HF_TOKEN"] = hf_token
    env["HUGGING_FACE_HUB_TOKEN"] = hf_token

    command = [
        sys.executable,
        "scripts/generate.py",
        prompt,
        "--model",
        "core8",
        "--duration",
        str(float(duration_seconds)),
        "--diffusion_steps",
        str(int(diffusion_steps)),
        "--history_frames",
        str(history_frames),
        "--seed",
        str(int(seed)),
        "--no-postprocess",
        "--output",
        output_name,
    ]
    result = subprocess.run(
        command, cwd=REPO_DIR, env=env, capture_output=True, text=True, timeout=110
    )
    if result.returncode != 0:
        tail = (result.stdout[-1500:] + "\n" + result.stderr[-1500:]).strip()
        raise gr.Error(f"ARDY generation failed:\n{tail}")

    npz_path = OUTPUT_DIR / f"{output_name}.npz"
    if not npz_path.exists():
        raise gr.Error("Generation finished but no output file was produced.")

    motion = np.load(npz_path, allow_pickle=False)
    joints = motion["posed_joints"]

    video_path = OUTPUT_DIR / f"{output_name}.mp4"
    render_skeleton_video(joints, video_path, fps=20)

    status = (
        f"Generated {joints.shape[0]} frames "
        f"({joints.shape[0] / 20:.1f}s at 20 FPS) with {joints.shape[1]} joints. "
        f"Seed: {int(seed)}."
    )
    return str(video_path), str(npz_path), status


BANNER_HTML = """
<div style='text-align: center; padding: 30px; background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%); border-radius: 15px; margin: 10px 0; box-shadow: 0 10px 30px rgba(0,0,0,0.3);'>
  <h1 style='color: #ffffff; margin: 0 0 8px 0; font-size: 2.3em;'>🏃 ARDY Motion Generator</h1>
  <h3 style='color: #c0c0ff; margin: 0 0 5px 0; font-weight: 400;'>NVIDIA ARDY (SIGGRAPH 2026) — Text-to-Motion, live on Hugging Face</h3>
  <p style='color: #aaa; margin: 0;'>Type a prompt, get a 3D human motion preview + raw .npz motion data</p>
</div>
<p align="center">
  <a href="https://www.youtube.com/@thebuildai?sub_confirmation=1"><img src="https://img.shields.io/badge/YouTube-SUBSCRIBE-red?style=for-the-badge&logo=youtube&logoColor=white" /></a>
  <a href="https://www.instagram.com/thebuildai/"><img src="https://img.shields.io/badge/Instagram-FOLLOW-E4405F?style=for-the-badge&logo=instagram&logoColor=white" /></a>
  <a href="https://www.tiktok.com/@the.build.ai"><img src="https://img.shields.io/badge/TikTok-FOLLOW-000000?style=for-the-badge&logo=tiktok&logoColor=white" /></a>
  <a href="https://github.com/cafermutluozkan/free-ai-notebooks"><img src="https://img.shields.io/badge/GitHub-FOLLOW-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>
"""

FOOTER_HTML = """
<div style="text-align: center; margin-top: 24px; border-top: 1px solid #333; padding-top: 16px;">
  <p style="color:#888; font-size: 13px;">
    Model: <a href="https://github.com/nv-tlabs/ardy" target="_blank">NVIDIA ARDY</a>
    (Apache 2.0 code / NVIDIA Open Model License weights) &middot;
    Want the full interactive Viser demo with kinematic constraints?
    <a href="https://github.com/cafermutluozkan/free-ai-notebooks" target="_blank">Run it free on Kaggle</a>.
  </p>
  <p style="color:#666; font-size: 12px;">🏃 ARDY Motion Generator — Built by
    <a href="https://www.thebuildai.tech/">TheBuildAI</a> 🌍
  </p>
</div>
"""

CSS = """
.gradio-container { max-width: 1000px !important; margin: auto !important; }
"""

with gr.Blocks(css=CSS, title="ARDY Motion Generator — TheBuildAI") as demo:
    gr.HTML(BANNER_HTML)

    with gr.Row():
        with gr.Column(scale=1):
            prompt_input = gr.Textbox(
                label="Motion prompt",
                placeholder="A person walks forward and waves with the right hand.",
                lines=3,
            )
            duration_slider = gr.Slider(
                1.0, 10.0, value=5.0, step=0.5, label="Duration (seconds)"
            )
            with gr.Accordion("Advanced settings", open=False):
                steps_slider = gr.Slider(
                    4, 30, value=10, step=1, label="Diffusion steps"
                )
                history_slider = gr.Slider(
                    4, 32, value=16, step=4, label="History frames (multiple of 4)"
                )
                seed_input = gr.Number(value=0, precision=0, label="Seed")
            generate_btn = gr.Button("🎬 Generate motion", variant="primary")
            gr.Markdown(
                "First request after a cold start can take several minutes "
                "(downloading Llama-3-8B + the ARDY checkpoint). Subsequent "
                "requests are much faster."
            )

        with gr.Column(scale=1):
            video_output = gr.Video(label="Generated motion preview")
            file_output = gr.File(label="Raw motion data (.npz)")
            status_output = gr.Textbox(label="Status", interactive=False)

    generate_btn.click(
        fn=generate_motion,
        inputs=[prompt_input, duration_slider, steps_slider, history_slider, seed_input],
        outputs=[video_output, file_output, status_output],
    )

    gr.HTML(FOOTER_HTML)

demo.queue(max_size=20).launch()
