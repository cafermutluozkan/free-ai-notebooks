# 🚀 Free AI Notebooks — Run Text-to-Video, TTS & Music on Free GPU

> **The largest collection of free, ready-to-run AI notebooks.** Run state-of-the-art models — Text-to-Video, Image-to-Video, Voice Cloning, Text-to-Speech, AI Music Generation — on **Kaggle**, **Google Colab**, **HuggingFace Spaces**, **Paperspace** & **Vast.ai**. Zero setup. One-click launch.

[![YouTube](https://img.shields.io/badge/YouTube-SUBSCRIBE-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/)
[![X](https://img.shields.io/badge/X-FOLLOW-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/)
[![Discord](https://img.shields.io/badge/Discord-JOIN-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/)

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

| Notebook | Description | Kaggle | Colab | HuggingFace | Video |
|:---|:---|:---:|:---:|:---:|:---:|
| **LTX-Video Generator (T2V + I2V)** | Lightricks LTX-Video (9B) via Diffusers. Text/Image-to-Video with audio mixing, gallery & OOM protection. | [![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?logo=kaggle&logoColor=white)](https://www.kaggle.com/) | [![Colab](https://img.shields.io/badge/Colab-F9AB00?logo=googlecolab&logoColor=white)](https://colab.research.google.com/) | [![HF](https://img.shields.io/badge/Spaces-FFD21E?logo=huggingface&logoColor=black)](https://huggingface.co/spaces/) | [![YouTube](https://img.shields.io/badge/Watch-FF0000?logo=youtube&logoColor=white)](https://youtu.be/) |

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

### HuggingFace Spaces
1. Click the **Spaces** badge
2. No GPU setup needed — runs on HF infrastructure
3. Use the web UI directly

### Paperspace / Vast.ai
- Free tier GPUs available. Upload the `.ipynb` file and run.

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
| HF Spaces | Free tier | — | Instant, no setup |
| Paperspace | Free RTX 4000 | — | Weekly free hours |
| Vast.ai | RTX 3090/4090 | — | Pay-per-hour, cheap |

---

## 📺 Video Tutorials

Each notebook has a dedicated YouTube tutorial. Click the **Watch** badge in the table above.

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
  <b>Free AI Notebooks — Built for the community 🌍</b><br>
  <!-- TODO: Add your own logo here -->
</p>
