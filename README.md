# TAAM: Track Any Aquatic Model

**TAAM** is a high-performance, professional-grade desktop application designed for the automated tracking and behavioral analysis of aquatic animals (Zebrafish, Medaka, Daphnia, etc.) in laboratory environments.

TAAM bridges the gap between large AI foundation models and real-time edge AI, combining:

🧠 **SAM 3 (Teacher Model)** — few-shot learning & automatic dataset generation  
⚡ **YOLO (Student Model)** — ultra-fast inference (100+ FPS) for real-time tracking

![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![AI](https://img.shields.io/badge/AI-SAM3%20%2B%20YOLO-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

<p align="center">
  <img src="https://github.com/yousaf2018/TAAM-Track-Any-Aquatic-Model/blob/main/source_code/assets/Logo.png" alt="TAAM Logo" width="200">
</p>

![TAAM GUI Snapshot](https://github.com/yousaf2018/TAAM-Track-Any-Aquatic-Model/blob/main/source_code/assets/TAAM-GUI.png)

---

## Acknowledgements

This application was developed in the **[Laboratory of Professor Chung-Der Hsiao](https://cdhsiao.weebly.com/pi-cv.html)** in collaboration with **Chung Yuan Christian University, Taiwan 🇹🇼**. Special credit and sincere gratitude are extended to **Professor Hsiao**, who shared his extensive research experience in biology and multiple domains, providing invaluable guidance and supervision throughout the development of this application.

<p align="center">
  <a href="https://www.cycu.edu.tw/">
    <img src="https://raw.githubusercontent.com/yousaf2018/EthoGrid/main/images/cycu.jpg" alt="Chung Yuan Christian University Logo" width="250">
  </a>
</p>

# 🌟 Key Features

- **Fully Automated AI Pipeline:** Train YOLO from just a few annotation clicks.
- **Teacher–Student Architecture:** SAM 3 generates accurate datasets → YOLO learns fast tracking.
- **YOLO-Only Mode:** Use existing SAM3 outputs to train YOLO directly.
- **Batch Video Processing:** Process dozens or hundreds of videos automatically.
- **Scientific Data Export:** High-precision CSVs with centroids, area, frame IDs, polygons, and image paths.
- **VRAM Optimization:** Video chunking + CPU offload for stable 4K processing.
- **Professional UI:** Dark-mode interface, side-by-side logging, and project event monitoring.

---

# 🚀 TAAM Workflow

## 1️⃣ PRE-PROCESSING
Split large lab videos into manageable segments for stable GPU processing.

## 2️⃣ ANNOTATION
Draw bounding boxes on a few frames. TAAM records them as few-shot prompts.

## 3️⃣ AI TRAINING PIPELINE

### 🧠 SAM 3 Stage
- Propagates masks across videos
- Tracks objects frame-by-frame
- Exports scientific CSV measurements
- Extracts frames to **sampling pool**: `Datasets/model_name/sampling_pool/`

> **Note:** Images are named to preserve video traceability: `OriginalVideoName_frame_000123.jpg`

### 🎯 YOLO Stage
- Cleans old train/val/test splits (but keeps `sampling_pool` intact)  
- Rebuilds dataset splits from sampling pool  
- Skips deleted SAM outputs  
- Handles first-time YOLO runs even if train/val/test folders do not exist  
- Supports Detection or Segmentation training automatically

## 4️⃣ DEPLOYMENT
Use trained models for high-speed tracking on new videos.

---

# 🗂️ Dataset Structure

```
Datasets/
└── model_name/
    ├── sampling_pool/
    ├── images/
    │   ├── train/
    │   ├── val/
    │   └── test/
    ├── labels/
    │   ├── train/
    │   ├── val/
    │   └── test/
    └── data.yaml
```

---

# 🛠️ Installation

TAAM can be installed inside your active Python virtual environment directly via `pip`. 

---

## 1. Create and Activate a Virtual Environment
It is highly recommended to install TAAM in an isolated environment using either Python `venv` or `conda`.

### Option A: Using Python venv
* **Windows (PowerShell):**
  ```powershell
  python -m venv taam_env
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass; .\taam_env\Scripts\Activate.ps1
  ```
* **Linux / macOS:**
  ```bash
  python3 -m venv taam_env
  source taam_env/bin/activate
  ```

### Option B: Using Conda
```bash
conda create -n taam_env python=3.10 -y
conda activate taam_env
```

---

## 2. Install PyTorch with GPU Support (Recommended)
Before installing the application, ensure that you install the version of PyTorch that matches your system's hardware to guarantee GPU-accelerated tracking.

* **For Windows/Linux (with CUDA 12.1):**
  ```bash
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
  ```
* **For Windows/Linux (with CUDA 11.8):**
  ```bash
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
  ```
* **For macOS / CPU-only installations:**
  ```bash
  pip install torch torchvision torchaudio
  ```

---

## 3. Install TAAM via pip
Run the following command to download and install the TAAM desktop application along with its dependencies:
```bash
pip install taam-tracker
```

---

## 4. Launch the Application
Once installed, you can start the desktop interface from your terminal at any time by running:
```bash
taam
```

---

# 🧠 First-Run Configuration (SAM 3 Setup)

When you run `taam` for the first time, your terminal will ask if you want to configure **SAM 3 Tracking**:

```text
=============================================================
           TAAM TRACKER - MODEL CONFIGURATION
=============================================================
To enable the SAM3 model, a Hugging Face Token is required.
If you skip this, only Ultralytics YOLO will be available.
-------------------------------------------------------------
Paste your Hugging Face Token (or press Enter to skip):
```

### Option A: Enable Full SAM 3 + YOLO Tracking
1. Create a free account on [Hugging Face](https://huggingface.co/).
2. Request access on the [SAM 3 (Segment Anything 3) Model Page](https://huggingface.co/).
3. Generate a token with at least **Read** permissions in your [Hugging Face Developer Settings](https://huggingface.co/settings/tokens).
4. Paste the token into your terminal and press **Enter**.
5. The application will log you in, download the local helper submodules, and launch. This setup is cached and will not prompt you again on subsequent runs.

### Option B: YOLO-Only Tracking Mode
1. Simply press **Enter** without pasting a token.
2. The installer will skip the SAM 3 configurations and launch immediately in YOLO-only mode.

---

## 🛠️ Commands Reference

| Task | Windows (PowerShell) | Linux / macOS (Terminal) |
|------|----------------------|------------------|
| **Create Environment** | `python -m venv taam_env` | `python3 -m venv taam_env` |
| **Activate Environment** | `.\\taam_env\\Scripts\\Activate.ps1` | `source taam_env/bin/activate` |
| **Install PyTorch** | *Use the cu121 or cu118 wheel links above* | `pip install torch` *(CPU or local default)* |
| **Install TAAM** | `pip install taam-tracker` | `pip install taam-tracker` |
| **Launch App** | `taam` | `taam` |

---

## ❓ Troubleshooting

### Re-triggering the Hugging Face / SAM 3 Prompt
If you skipped the token configuration on your first launch but want to set up SAM 3 now:
1. Delete your local Hugging Face credentials cache:
   * **Windows:** Delete the folder `C:\\Users\\YourUsername\\.cache\\huggingface\\`
   * **Linux / macOS:** Delete the directory `~/.cache/huggingface/`
2. Run `taam` in your terminal to see the token configuration prompt again.

### PyQt6 DLL Load Errors (Windows Conflicts)
PyQt6 can conflict with secondary graphical engines (like OBS Studio, Anaconda distributions, or external media drivers). 
* **Solution:** The `taam-tracker` package contains an automatic path correction engine that sanitizes your active environment runtime. Ensure you are running the app inside your dedicated virtual environment by calling `taam` in your terminal.

### PyTorch says GPU is Unavailable (`CUDA is False`)
1. Ensure your computer has a compatible NVIDIA GPU.
2. Install the latest official GPU drivers directly from [nvidia.com](https://www.nvidia.com/).
3. Re-run your corresponding PyTorch installation command with the `--force-reinstall` flag to make sure the CPU version was not cached.

---

# 📄 License
MIT License

---

# 👨‍🔬 Author
**Mahmood Yousaf**  
PhD Researcher — Biomedical Engineering  
Chung Yuan Christian University, Taiwan
