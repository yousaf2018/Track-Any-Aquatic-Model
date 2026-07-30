# TAAM: Track Any Aquatic Model

**TAAM** is a high-performance, professional-grade desktop application designed for the automated tracking and behavioral analysis of aquatic animals in laboratory environments.

TAAM bridges the gap between large AI foundation models and real-time edge AI, combining:

🧠 **SAM 3 (Teacher Model)** — few-shot learning & automatic dataset generation  
⚡ **YOLO (Student Model)** — ultra-fast inference (100+ FPS) for real-time tracking

![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
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

# 🖥️ Hardware Prerequisite: NVIDIA GPU & CUDA Setup

To run the SAM 3 and YOLO pipelines with GPU acceleration, you must have an NVIDIA GPU and verify your graphics drivers before installing TAAM.

### Step 1: Install Latest NVIDIA Drivers
1. Go to the [Official NVIDIA Driver Downloads Page](https://www.nvidia.com/Download/index.aspx).
2. Select your Product Type, Product Series, and Operating System.
3. Download and install the latest **Game Ready Driver** or **Studio Driver**.
4. Restart your computer after installation completes.

### Step 2: Verify Your System's Driver Status
Open your command prompt or terminal and run:
```bash
nvidia-smi
```
If your drivers are installed correctly, this command will output your GPU's current status and the highest supported CUDA Version (e.g., CUDA 12.1 or CUDA 11.8).

---

# 🛠️ Installation Pathways

Choose **one** of the three installation pathways below based on your workflow. Option 1 is highly recommended for standard users.

---

## 📦 Option 1: Quick Install via PyPI (Recommended / Zero-Clone)
This method is the easiest deployment option. It uses the package manager to download the app directly. You do not need to clone the repository manually; the package will handle everything on your first launch.

### 1. Create and Activate a Virtual Environment
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

### 2. Install PyTorch with GPU Support
Install the PyTorch wheels matching your active CUDA runtime:
* **For CUDA 12.1:**
  ```bash
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
  ```
* **For CUDA 11.8:**
  ```bash
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
  ```

### 3. Install TAAM and Run
Download the application and start it:
```bash
pip install taam-tracker
taam
```
*(On your first launch, the app will ask for your Hugging Face Token in the terminal and configure the remaining resources automatically).*

---

## 🪟 Option 2: Automated Batch Scripts (Windows Local Source)
If you prefer running the application from the local cloned source code, you can use automated Windows scripts.

### 1. Clone the Repository
Open PowerShell and run:
```powershell
git clone https://github.com/yousaf2018/TAAM.git
cd TAAM/source_code
```

### 2. Run the Scripts
* **Step 1:** Double-click **`INSTALLER.bat`**. This script checks your environment, installs PyTorch with CUDA, compiles local submodules, and configures Hugging Face authentication.
* **Step 2:** Use **`RUNNER.bat`** to launch the desktop application. This script cleans up runtime environmental conflicts automatically.

---

## 🐧 Option 3: Manual Installation from Source (Step-by-Step)
For developers or users running manual source builds on Windows or Linux.

### 1. Clone and Enter Directory
```bash
git clone https://github.com/yousaf2018/TAAM.git
cd TAAM/source_code
```

### 2. Setup the Environment
* **Windows (PowerShell):**
  ```powershell
  python -m venv sam3_tracker_venv
  .\\sam3_tracker_venv\\Scripts\\Activate.ps1
  ```
* **Linux (Terminal):**
  ```bash
  python3 -m venv sam3_tracker_venv
  source sam3_tracker_venv/bin/activate
  ```

### 3. Install PyTorch with CUDA
* **For Windows (PowerShell):**
  Try CUDA 12.1 first:
  ```powershell
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
  python -c "import torch; print('CUDA 12.1 Working:', torch.cuda.is_available())"
  ```
  If it returns `False`, fall back to CUDA 11.8:
  ```powershell
  pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
  python -c "import torch; print('CUDA 11.8 Working:', torch.cuda.is_available())"
  ```
* **For Linux:**
  ```bash
  pip install torch torchvision torchaudio
  ```

### 4. Install Dependencies & Submodules
* **Windows (PowerShell):**
  ```powershell
  pip install -r requirements-win.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
  pip install -e ./sam3
  ```
* **Linux (Terminal):**
  ```bash
  pip install -r requirements.txt
  pip install -e ./sam3
  ```

### 5. Hugging Face Login
```bash
python -c "from huggingface_hub import login; login(token='YOUR_TOKEN_HERE')"
```

### 6. Launch the App
* **Windows:** `python main.py`
* **Linux:** `python3 main.py`

---

# 🛠️ Summary of Commands for Option 3 Quick Copy

| Task | Windows (PowerShell) | Linux (Terminal) |
|------|----------------------|------------------|
| **Clone** | `git clone https://github.com/yousaf2018/TAAM.git` | Same |
| **Venv** | `python -m venv sam3_tracker_venv` | `python3 -m venv sam3_tracker_venv` |
| **Activate** | `.\\sam3_tracker_venv\\Scripts\\Activate.ps1` | `source sam3_tracker_venv/bin/activate` |
| **Torch** | *Use CUDA wheel links above* | `pip install torch` |
| **Requirements** | `pip install -r requirements-win.txt` | `pip install -r requirements.txt` |
| **Local Mod** | `pip install -e ./sam3` | Same |
| **Launch** | `python main.py` | `python3 main.py` |

---

# ❓ Troubleshooting

### DLL Load Failed (Windows)
PyQt6 can conflict with system-level Qt directories (like Anaconda or OBS Studio). 
* **Solution:** If running from source, clean your path before running `main.py`:
  ```powershell
  $env:PATH = "C:\\Windows\\system32;C:\\Windows;D:\\path\\to\\your\\project\\sam3_tracker_venv\\Scripts"
  python main.py
  ```
  *(If you installed via **Option 1**, this cleanup is handled programmatically behind the scenes).*

### Hugging Face Login Hangs
If the interactive CLI login hangs, use the non-interactive inline login method:
```bash
python -c "from huggingface_hub import login; login(token='your_token_here')"
```

### CUDA `torch.cuda.is_available()` returns False
1. Verify that your graphics card is listed inside your device manager.
2. Confirm that you have installed the latest NVIDIA drivers matching your hardware.
3. Re-run your corresponding PyTorch installation command with the `--force-reinstall` flag to overwrite any cached CPU-only builds.

---

# 📄 License
MIT License

---

# 👨‍🔬 Author
**Mahmood Yousaf**  
PhD Researcher — Biomedical Engineering  
Chung Yuan Christian University, Taiwan
