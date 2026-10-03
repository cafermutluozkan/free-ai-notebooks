# 🚀 Free AI Notebooks — Image Upscaler (4K), Text-to-Video, TTS & Music on Free GPU

> **The largest collection of free, ready-to-run AI notebooks.** Run state-of-the-art models — **AI Image Upscaling & Restoration (4K)**, Text-to-Image, Text-to-Video, Image-to-Video, 3D Gaussian Splat, Text-to-Motion, Voice Cloning, Text-to-Speech, AI Music Generation — on **Kaggle**, **Google Colab**, **Lightning AI**, **HuggingFace Spaces**, **Paperspace** & **Vast.ai**. Zero setup. One-click launch. Free T4 GPU.

**Quick links:** [HYPIR Image Upscaler](#-hypir-ai-image-upscaler-4k--featured) · [All notebooks](#-notebooks) · [Quick start](#-quick-start) · [FAQ](#-faq)

[![YouTube](https://img.shields.io/badge/YouTube-SUBSCRIBE-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@thebuildai)
[![Instagram](https://img.shields.io/badge/Instagram-FOLLOW-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/thebuildai/)
[![TikTok](https://img.shields.io/badge/TikTok-FOLLOW-000000?style=for-the-badge&logo=tiktok&logoColor=white)](https://www.tiktok.com/@the.build.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-CONNECT-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/cafermutluozkan/)
[![Web](https://img.shields.io/badge/Web-VISIT-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)](https://www.thebuildai.tech/)

---

## 🎯 What's Inside

| Category | Models | Modes |
|---|---|---|
| **🖼️ Image Upscaling & Restoration** | HYPIR (SD 2.1 + LoRA) | Single-pass 4K upscale, photo restoration, optional text prompt |
| **🎨 Text-to-Image** | Krea-2-Turbo | 8-step fast generation, style presets |
| **🧊 3D** | TripoSplat | Single image → 3D Gaussian Splat |
| **🕺 Motion** | NVIDIA ARDY | Real-time text-to-motion |
| **🎬 Video Generation** | LTX-Video, Wan2.1, HunyuanVideo | Text-to-Video, Image-to-Video, First/Last Frame |
| **🗣️ Voice & Speech** | VoxCPM2, OmniVoice, MOSS-TTS, Qwen3-TTS | Voice Cloning, Text-to-Speech, Voice Design |
| **🎵 Music Generation** | ACE-Step, HeartMuLa | AI Music, LoRA Training |
| **📝 Transcription** | Cohere Transcribe | ASR, 14+ Languages |
| **🎭 Talking Head** | SoulX FlashHead | Audio-Driven Avatar |

All notebooks include **Gradio web UI**, **progress bars**, **error handling** and **smart GPU memory management**.

---

## 🖼️ HYPIR AI Image Upscaler (4K) — Featured

**Free AI image upscaler & photo restoration** powered by [HYPIR](https://github.com/XPixelGroup/HYPIR) (SIGGRAPH Asia 2025). It restores and upscales low-quality images to **4K in a single forward pass** — no slow iterative diffusion sampling — by fine-tuning a Stable Diffusion 2.1 prior with adversarial training.

- ⚡ **Single-pass** restoration & upscaling (1×–8× factor, output capped at 4096×4096)
- 📐 **Auto-resize:** oversized inputs (e.g. 8000×6000) are automatically downscaled so the result fits the 4K cap — no more "exceeds the 4K safety limit" errors
- ✍️ **Optional text prompt** to guide fine detail (e.g. *sharp facial features, fine skin texture*)
- 🔍 **Before / After comparison slider** in the Gradio UI
- 🖥️ Runs on a **free T4 GPU** — Kaggle, Google Colab and Lightning AI versions

| Platform | Notebook | Launch |
|:---|:---|:---:|
| Kaggle (T4 x1) | [`hypir-image-upscaler-kaggle-t4.ipynb`](notebooks/hypir-image-upscaler-kaggle-t4.ipynb) | [![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/code/cafermutluzkan/hypir-ai-image-upscaler-4k-t4-gpu) |
| Google Colab (T4) | [`hypir-image-upscaler-colab.ipynb`](notebooks/hypir-image-upscaler-colab.ipynb) | [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://drive.google.com/file/d/1GGSiW4d63TraTpC9omZj7Up9nVr7iCM4/view?usp=sharing) |
| Lightning AI | [`hypir-image-upscaler-lightning.ipynb`](notebooks/hypir-image-upscaler-lightning.ipynb) | _link coming soon_ |

> ⚠️ **License:** HYPIR code and weights are **non-commercial only** ([details](https://github.com/XPixelGroup/HYPIR/blob/main/LICENSE)). The notebook code in this repo is MIT, but the model it downloads is not.

📄 Paper: [arXiv:2507.20590](https://arxiv.org/abs/2507.20590) · 🤗 Weights: [lxq007/HYPIR](https://huggingface.co/lxq007/HYPIR)

---

## 📓 Notebooks

| Notebook | Description | Kaggle | Colab | Lightning AI | HuggingFace | Video |
|:---|:---|:---:|:---:|:---:|:---:|:---:|
| **HYPIR Image Upscaler (4K)** | HYPIR (SIGGRAPH Asia 2025) single-pass image restoration & upscaling up to 4K, fine-tuned SD 2.1 + LoRA with adversarial training (no iterative diffusion sampling). Auto-resizes oversized inputs, optional text prompts, interactive before/after comparison slider. Non-commercial model license. | [![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/code/cafermutluzkan/hypir-ai-image-upscaler-4k-t4-gpu) | [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://drive.google.com/file/d/1GGSiW4d63TraTpC9omZj7Up9nVr7iCM4/view?usp=sharing) | — | [![HF](https://img.shields.io/badge/Model-FFD21E?logo=huggingface&logoColor=black)](https://huggingface.co/lxq007/HYPIR) | — |
| **ARDY Motion Generator** | NVIDIA ARDY (SIGGRAPH 2026) real-time text-to-motion on free Kaggle Dual T4 GPUs. Autoregressive diffusion streams 3D human motion from text prompts, with a Llama-3-8B (LLM2Vec) text encoder on GPU 1, T4 FP16 compatibility patch, automatic CPU fallback, and an optional Cloudflare-tunneled interactive Viser demo. | [![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/code/cafermutluzkan/nvidia-ardy-text-to-motion-free-kaggle-dual-t4) | — | — | [![HF](https://img.shields.io/badge/Model-FFD21E?logo=huggingface&logoColor=black)](https://huggingface.co/collections/nvidia/ardy) | [![YouTube](https://img.shields.io/badge/YouTube-FF0000?logo=youtube&logoColor=white)](https://youtu.be/kY9E12yiR4Y?si=ActdzimEoD_0tnr_) |
| **Krea-2-Turbo** | Krea-2-Turbo 12B INT8 via Wan2GP + mmgp. Fast Text-to-Image in 8 steps with style presets, prompt enhancer and batch generation. | [![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/code/cafermutluzkan/krea-2-turbo-text-to-image-model-kaggle-edition) | [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://drive.google.com/file/d/1oLevYcr60hEwqXWSujkiaKicM120LhnA/view?usp=sharing) | [![Lightning](https://img.shields.io/badge/Lightning-792EE5?logo=lightning&logoColor=white)](https://lightning.ai/thebuildai-org/templates/krea-2-turbo-text-to-image-model) | [![HF](https://img.shields.io/badge/Model-FFD21E?logo=huggingface&logoColor=black)](https://huggingface.co/krea/Krea-2-Turbo) | [![YouTube](https://img.shields.io/badge/YouTube-FF0000?logo=youtube&logoColor=white)](https://youtu.be/8zw2J4343O4) |
| **LTX-Video Generator (T2V + I2V)** | LTX-2.3 22B Distilled via Wan2GP + mmgp. Text/Image-to-Video with progress bar, gallery & OOM protection. | [![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/code/cafermutluzkan/ltx-video-generator-kaggle-t4-gpu-edition) | [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://drive.google.com/file/d/1znYoCpBGv3O0wyW7w1Omwj5TGohzjks2/view?usp=sharing) | [![Lightning](https://img.shields.io/badge/Lightning-792EE5?logo=lightning&logoColor=white)](https://lightning.ai/thebuildai/templates/ltx-video-generator) | [![HF](https://img.shields.io/badge/Model-FFD21E?logo=huggingface&logoColor=black)](https://huggingface.co/Lightricks/LTX-2.3) | [![YouTube](https://img.shields.io/badge/YouTube-FF0000?logo=youtube&logoColor=white)](https://youtu.be/-0SQEHFX7ZE?si=j818TnRli1aBIf7i) |
| **TripoSplat** | VAST-AI TripoSplat — single image to 3D Gaussian Splat. Interactive 3D viewer in Gradio. | [![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/code/cafermutluzkan/triposplat-kaggle-t4-gpu-edition) | [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://drive.google.com/file/d/1kUCLaLLL0XbJ7h3IfB1oixKQN7GL8eGe/view?usp=sharing) | [![Lightning](https://img.shields.io/badge/Lightning-792EE5?logo=lightning&logoColor=white)](https://lightning.ai/thebuildai/templates/triposplat) | [![HF](https://img.shields.io/badge/Demo-FFD21E?logo=huggingface&logoColor=black)](https://huggingface.co/spaces/VAST-AI/TripoSplat) | [![YouTube](https://img.shields.io/badge/YouTube-FF0000?logo=youtube&logoColor=white)](https://youtu.be/C3SbmpUbz4M?si=w7O2cn-rQGWJoRfO) |

---

## ⚡ Quick Start

### Kaggle (Recommended for Video)
1. Click the **Kaggle** badge → "Copy & Edit"
2. **Settings → Accelerator → GPU T4 x1**
3. **Settings → Internet → ON**
4. Click **Run All**
5. Wait for the **Gradio public URL** in the output

### Google Colab
1. Click the **Colab** badge
2. **Runtime → Change runtime type → T4 GPU**
3. **Runtime → Run All**
4. Wait for the **Gradio public URL**

### Lightning AI
1. Click the **Lightning** badge
2. Open in GPU Studio (T4 or L4)
3. Run cells in order
4. Wait for the **Gradio public URL**

### HuggingFace Spaces
1. Click the **Spaces** badge
2. No GPU setup needed — runs on HF infrastructure
3. Use the web UI directly

---

## 💡 Pro Tips

- **First run downloads models** (~5-20 GB). Subsequent runs use cache.
- **VRAM running out?** Lower resolution (512×512) or reduce frames (25).
- **Want faster generation?** Reduce inference steps (15-20).
- **Need longer videos?** Use frame interpolation tools after generation.
- **Colab "Torch not compiled with CUDA enabled"?** No GPU is attached — *Runtime → Change runtime type → T4 GPU*, then restart the session.

---

## 🔧 Requirements

| Platform | GPU | RAM | Notes |
|---|---|---|---|
| Kaggle | T4 / P100 | 30 GB | Best for video models |
| Google Colab | T4 | 12 GB | Good for TTS & music |
| Lightning AI | T4 / L4 | 15-30 GB | GPU Studio, free tier |
| HF Spaces | Free tier | — | Instant, no setup |

---

## ❓ FAQ

**Is there a free AI image upscaler that runs on Kaggle or Colab?**
Yes — the HYPIR notebooks above upscale and restore images up to 4K on a free T4 GPU with a Gradio web UI.

**Why does my 8000×6000 image get resized?**
Output is capped at 4096×4096 so a single T4 doesn't run out of memory. The notebook now downscales the input automatically to fit; use a lower upscale factor (1×–2×) for very large photos.

**Can I use the results commercially?**
HYPIR's code and weights are non-commercial only. Check each model's license before commercial use.

**Do I need to install anything?**
No. Everything runs in the browser on Kaggle, Colab or Lightning AI — just enable a GPU.

---

## 📺 Video Tutorials

Each notebook has a dedicated YouTube tutorial on [@thebuildai](https://www.youtube.com/@thebuildai). Subscribe for step-by-step walkthroughs.

---

## ⭐ Star History

If you find this useful, please ⭐ the repo. It helps more people discover free AI tools.

---

## 🤝 Contributing

1. Fork the repo
2. Add your notebook to `notebooks/`
3. Update the table in README.md
4. Submit a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 📜 License

Notebook code is open-source under [MIT License](LICENSE). Models downloaded by the notebooks keep their own licenses (e.g. HYPIR is non-commercial only).

---

<p align='center'>
  <a href='https://www.youtube.com/@thebuildai'><img src='https://img.shields.io/badge/YouTube-SUBSCRIBE-red?logo=youtube&logoColor=white' height='24'></a>
  <a href='https://www.instagram.com/thebuildai/'><img src='https://img.shields.io/badge/Instagram-FOLLOW-E4405F?logo=instagram&logoColor=white' height='24'></a>
  <a href='https://www.tiktok.com/@the.build.ai'><img src='https://img.shields.io/badge/TikTok-FOLLOW-000000?logo=tiktok&logoColor=white' height='24'></a>
  <a href='https://github.com/cafermutluozkan'><img src='https://img.shields.io/badge/GitHub-FOLLOW-181717?logo=github&logoColor=white' height='24'></a>
  <a href='https://www.linkedin.com/in/cafermutluozkan/'><img src='https://img.shields.io/badge/LinkedIn-CONNECT-0A66C2?logo=linkedin&logoColor=white' height='24'></a>
  <br><br>
  <b>Free AI Notebooks — Built by <a href='https://www.thebuildai.tech/'>TheBuildAI</a> 🌍</b>
</p>
