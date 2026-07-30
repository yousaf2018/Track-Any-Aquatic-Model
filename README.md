# TAAM: Track Aquatic Animal Model

**TAAM** is a high-performance, professional-grade desktop application designed for the automated tracking and behavioral analysis of aquatic animals

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

# 📖 Detailed Modules & Usage Guide

TAAM is structured into five core modules accessible via the left sidebar and main tab widget. This design allows researchers to seamlessly transition from raw video handling to advanced behavioral statistical analysis.

### 📁 The Workspace Directory Concept
Before running any analysis, the user must select a workspace folder using the sidebar. This folder acts as the central database of the application. All temporary files, exported datasets, trained model weights, and the default settings file are organized here. 

```text
TAAM_Workspace/
├── Datasets/           # Automatically generated YOLO training data
├── Experiments/        # Raw tracking CSVs and annotated videos
├── Models/             # Trained .pt weights categorized by version
└── endpoints.json      # Saved parameters and zone configurations
```

---

### ✂️ Module 1: Video Pre-Processor (Splitter)
Continuous twenty four hour video files contain millions of frames, creating a major data burden. Loading these massive files directly into neural networks like SAM 3 will cause instant memory crashes.
1.  Navigate to **Tab 1: SPLIT**.
2.  Click **Add Huge Videos** to load raw recordings into the queue.
3.  Set the **Split Seconds** (default is sixty seconds).
4.  Select a target directory and click **Start Batch Splitting**.
The engine uses high speed parallel processing to slice your large files into contiguous, VRAM safe segments without dropping a single frame.

---

### 🎨 Module 2: Few-Shot Annotation Canvas
This module allows researchers to "teach" the AI what to track using only three to five initial frames, bypassing the need for manual data labeling.
1.  Select a splitted video from your sidebar list.
2.  Type your target species as a comma separated list (e.g., `zebrafish, medaka`) in the class input field. The active label dropdown will automatically update.
3.  Use the horizontal slider to find a frame containing clear views of your subjects.
4.  Draw a bounding box around each animal. Use the shortcuts **Ctrl+C** to copy a box and **Ctrl+V** to paste it onto the next frame. Use **Delete** to remove a mistake.
Your annotations are automatically synced in the background to prevent data loss.

---

### 🧠 Module 3: Teacher-Student AI Training Pipeline
This module executes the automated knowledge distillation. The expert segmentation capabilities of a heavy foundation model are transferred into a lightweight, high speed edge model.
1.  Navigate to **Tab 3: TRAIN**.
2.  Input a unique name for your project to ensure correct versioning.
3.  Select your target task type: **Detection** (for standard speed tracking) or **Segmentation** (for precise polygon mask training).
4.  Adjust your parameters: set the maximum frames to sample and adjust the Train/Val/Test split sliders (the UI automatically balances them to ensure they always sum to one hundred percent).
5.  Click **Launch Full Auto Pipeline**. 
*   **The SAM 3 Teacher** propagates your annotations across the chunks, exporting coordinate data and writing frame JPEGs to a raw pool.
*   **The YOLO Student** then randomly samples those frames, splits them scientifically into training folders, and fine tunes itself completely in the background.

---

### 📐 Module 4: Advanced Arena (ROI) Designer
For multi tank or multi well plate assays, researchers must segregate tracking data by individual container. This tab is used to define the geometric boundaries of each tank.
1.  Navigate to **Tab 4: ADVANCED**.
2.  Choose your arena type from the dropdown: **Rectangle**, **Circle**, or **Grid**.
3.  For a multi well plate (e.g., cichlid tanks or zebrafish larvae), select **Grid** and input the row and column count (e.g., $2 \times 2$).
4.  Draw the shape over your video. Use the transformation sliders in the sidebar to adjust width, height, and rotation to compensate for camera lens tilt.
The system automatically splits grids into individual wells and indexes them from left to right, then top to bottom, ensuring the Excel sheets match your physical setup.

---

### 📈 Module 5: Behavioral Endpoints & Analytics Suite
This is the scientific mission control popup designed to extract clinical endpoints from your raw tracking CSVs without any data preprocessing or filtering.

1.  Click the large green **Behavioral Analysis** button in the sidebar to open the dedicated analysis window.
2.  **Create Groups:** Click "Create Group" and name them manually (e.g., *Control*, *Treated_Dose_A*). Select a group and click "Add CSV" to import the TAAM tracked files.
3.  **Load ROI:** Click "Load ROI Designer JSON" to import your tank boundaries.
4.  **Auto-Fill Metadata:** Click "Load Video". The system will automatically read the FPS and calculate the Duration from the file, filling in the parameters for you.
5.  **Adjust Zones:** Select "Arena 1" from the dropdown. Move the sliders to define the vertical center line of the tank. The left side is calculated as the Top portion, and the right side is the Bottom portion (lateral view logic). Adjust each arena individually.
6.  **Checklist:** Check or uncheck the specific behavioral endpoints you want to extract for your manuscript.
7.  **Generate Report:** Click "Generate Scientific Report". The engine calculates all endpoints and saves a consolidated, publication ready CSV named after your files.

#### Mathematical Formulations calculated in the Module:
*   **Average Speed (cm/s):** $\bar{v} = \frac{1}{N} \sum_{i=1}^{N} v_{i}$
*   **Time in Top / Bottom (%):** $Z_{top} = \frac{\text{Count}(x_{i} < X_{split})}{N} \times 100$
*   **Average Thigmotaxis (cm):** $D_{CL} = \frac{1}{N} \sum_{i=1}^{N} \frac{|x_{i} - X_{split}|}{C}$
*   **Shannon Entropy (Hartleys):** $H = -\sum_{j=1}^{M} P_{j} \log_{10}(P_{j})$ *(Uses a base-10 log and 10x10 grid to constrain values to a clean scientific range of 0.9 to 1.1)*.
*   **Fractal Dimension:** Slope of the log-log regression of the correlation integral using exact 0.1 to 3.1 r-steps.

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
  Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass; .\sam3_tracker_venv\Scripts\Activate.ps1
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
