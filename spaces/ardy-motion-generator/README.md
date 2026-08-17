---
title: ARDY Motion Generator
emoji: 🏃
colorFrom: indigo
colorTo: purple
sdk: gradio
app_file: app.py
pinned: false
license: apache-2.0
short_description: NVIDIA ARDY (SIGGRAPH 2026) real-time text-to-motion demo
tags:
  - nvidia
  - ardy
  - text-to-motion
  - motion-generation
  - human-motion
  - diffusion
  - pytorch
  - gradio
---

# 🏃 ARDY Motion Generator — TheBuildAI

Free, always-on demo of **NVIDIA ARDY** (SIGGRAPH 2026) — an autoregressive
diffusion model for real-time, text-conditioned 3D human motion generation.
Type a prompt (e.g. *"A person walks forward and waves with the right
hand."*) and get back a short animated preview plus the raw motion data
(`.npz`: posed joints, rotations, foot contacts).

- **Model:** [NVIDIA ARDY](https://github.com/nv-tlabs/ardy) — Core skeleton,
  20 FPS, Horizon 8 (`core8`)
- **Text encoder:** LLM2Vec on `meta-llama/Meta-Llama-3-8B-Instruct`
- **Paper:** [research.nvidia.com/labs/sil/projects/ardy](https://research.nvidia.com/labs/sil/projects/ardy/)
- **Weights:** [huggingface.co/collections/nvidia/ardy](https://huggingface.co/collections/nvidia/ardy)
- **License:** inference code Apache 2.0; model weights under the
  [NVIDIA Open Model License](https://huggingface.co/nvidia/ARDY-Core-RP-20FPS-Horizon8)
  (commercial use permitted)

This Space renders a lightweight joint-scatter animation for a quick
preview. For the **full interactive experience** — live Viser 3D viewer,
kinematic constraints (paths, waypoints, keyframes), and dual-GPU setup — run
our free Kaggle notebook instead:

👉 [ARDY on Kaggle (Dual T4, free GPU)](https://github.com/cafermutluozkan/free-ai-notebooks)

## Space owner setup

This Space needs a Hugging Face token with **approved access** to
[`meta-llama/Meta-Llama-3-8B-Instruct`](https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct):

1. Request access on the model page and wait for approval.
2. Create a read token in [HF token settings](https://huggingface.co/settings/tokens).
3. In this Space: **Settings → Repository secrets → New secret** → name
   `HF_TOKEN`, value = your token.

First launch clones `nv-tlabs/ardy` and builds its C++ extension, then
downloads Llama-3-8B (~16 GB) and the ARDY checkpoint on the first
generation call — the first request after a cold start can take several
minutes. Subsequent requests are much faster.

---

<p align="center">
  <a href="https://www.youtube.com/@thebuildai?sub_confirmation=1"><img src="https://img.shields.io/badge/YouTube-SUBSCRIBE-red?style=for-the-badge&logo=youtube&logoColor=white" /></a>
  <a href="https://www.instagram.com/thebuildai/"><img src="https://img.shields.io/badge/Instagram-FOLLOW-E4405F?style=for-the-badge&logo=instagram&logoColor=white" /></a>
  <a href="https://www.tiktok.com/@the.build.ai"><img src="https://img.shields.io/badge/TikTok-FOLLOW-000000?style=for-the-badge&logo=tiktok&logoColor=white" /></a>
  <a href="https://github.com/cafermutluozkan/free-ai-notebooks"><img src="https://img.shields.io/badge/GitHub-FOLLOW-181717?style=for-the-badge&logo=github&logoColor=white" /></a>
</p>

<p align="center">Built by <a href="https://www.thebuildai.tech/">TheBuildAI</a> 🌍</p>
