# 🚀 Free AI Notebooks — Run Text-to-Video, TTS & Music on Free GPU

> **The largest collection of free, ready-to-run AI notebooks.** Run state-of-the-art models — Text-to-Video, Image-to-Video, Voice Cloning, Text-to-Speech, AI Music Generation — on **Kaggle**, **Google Colab**, **HuggingFace Spaces**, **Paperspace** & **Vast.ai**. Zero setup. One-click launch.

[![YouTube](https://img.shields.io/badge/YouTube-SUBSCRIBE-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@thebuildai)
[![Instagram](https://img.shields.io/badge/Instagram-FOLLOW-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/thebuildai/)
[![TikTok](https://img.shields.io/badge/TikTok-FOLLOW-000000?style=for-the-badge&logo=tiktok&logoColor=white)](https://www.tiktok.com/@the.build.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-CONNECT-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/cafermutluozkan/)
[![Web](https://img.shields.io/badge/Web-VISIT-4285F4?style=for-the-badge&logo=googlechrome&logoColor=white)](https://www.thebuildai.tech/)

---

## 🎯 What's Inside

| Category | Models | Modes |
|---|---|---|
| **🎬 Video Generation** | LTX-Video, Wan2.1, HunyuanVideo | Text-to-Video, Image-to-Video, First/Last Frame |
| **🗣️ Voice & Speech** | VoxCPM2, OmniVoice, MOSS-TTS, Qwen3-TTS | Voice Cloning, Text-to-Speech, Voice Design |
| **🎵 Music Generation** | ACE-Step, HeartMuLa | AI Music, LoRA Training |
| **📝 Transcription** | Cohere Transcribe | ASR, 14+ Languages |
| **🎭 Talking Head** | SoulX FlashHead | Audio-Driven Avatar |

All notebooks include **Gradio web UI**, **progress bars**, **error handling** and **smart GPU memory management**.

---

## 📓 Notebooks

| Notebook | Description | Kaggle | Colab | Lightning AI | HuggingFace |
|:---|:---|:---:|:---:|:---:|:---:|
| **LTX-Video Generator (T2V + I2V)** | LTX-2.3 22B Distilled via Wan2GP + mmgp. Text/Image-to-Video with progress bar, gallery & OOM protection. | [![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/code/cafermutluzkan/ltx-video-generator) | [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://drive.google.com/file/d/1H3yZrwQt6KZs8Bbyetjo8WCR8MsEeaUO/view?usp=sharing) | [![Lightning](https://img.shields.io/badge/Lightning-792EE5?logo=lightning&logoColor=white)](https://lightning.ai/thebuildai/templates/ltx-video-generator) | [![HF](https://img.shields.io/badge/Model-FFD21E?logo=huggingface&logoColor=black)](https://huggingface.co/Lightricks/LTX-2.3) |
| **TripoSplat** | VAST-AI TripoSplat — single image to 3D Gaussian Splat. Interactive 3D viewer in Gradio. | [![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/code/cafermutluzkan/triposplat) | [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://drive.google.com/file/d/1D4tGY13NedBrx-rMrI2Mc3rOb-zuKvNH/view?usp=sharing) | [![Lightning](https://img.shields.io/badge/Lightning-792EE5?logo=lightning&logoColor=white)](https://lightning.ai/thebuildai/templates/triposplat) | [![HF](https://img.shields.io/badge/Demo-FFD21E?logo=huggingface&logoColor=black)](https://huggingface.co/spaces/VAST-AI/TripoSplat) |

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

---

## 🔧 Requirements

| Platform | GPU | RAM | Notes |
|---|---|---|---|
| Kaggle | T4 / P100 | 30 GB | Best for video models |
| Google Colab | T4 | 12 GB | Good for TTS & music |
| Lightning AI | T4 / L4 | 15-30 GB | GPU Studio, free tier |
| HF Spaces | Free tier | — | Instant, no setup |

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

All notebooks are open-source under [MIT License](LICENSE).

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
