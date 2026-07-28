# taam/main.py
import os
import sys
import multiprocessing
from pathlib import Path

# 1. PATH FIX: Insert the directory of this file into sys.path.
# This prevents broken imports inside your package (e.g. from gui.main_window import ...)
CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

# CRITICAL: Fix for Multi-class and YOLO Core Dumps
if sys.platform.startswith('linux') or sys.platform.startswith('win'):
    try:
        multiprocessing.set_start_method("spawn", force=True)
    except RuntimeError: 
        pass

# Graphics & CUDA Allocator Optimization Settings
os.environ["CUBLAS_WORKSPACE_CONFIG"] = ":4096:8"
os.environ["PYTORCH_CUDA_ALLOC_CONF"] = "expandable_segments:True"


# --- SYSTEM LOGIC WORKAROUNDS ---

def fix_windows_dll_path():
    """ Keeps PyQt6 safe from DLL conflicts on Windows """
    if sys.platform == "win32":
        venv_path = sys.prefix
        venv_scripts = os.path.join(venv_path, "Scripts")
        system32 = os.path.join(os.environ.get("SystemRoot", "C:\\Windows"), "System32")
        windows_dir = os.environ.get("SystemRoot", "C:\\Windows")
        clean_paths = [venv_scripts, system32, windows_dir]
        for path in os.environ.get("PATH", "").split(";"):
            if path and not any(conflict in path.lower() for conflict in ["anaconda", "miniconda", "obs-studio", "qt"]):
                clean_paths.append(path)
        os.environ["PATH"] = ";".join(clean_paths)

def install_local_sam3():
    """
    Programmatically runs pip to install the local sam3 submodule
    into the active virtual environment at runtime.
    """
    import subprocess
    print("\n[*] Installing local SAM3 modules...")
    
    # Path calculation assuming layout:
    # root_folder/taam/main.py -> root_folder/sam3
    sam3_path = os.path.abspath(os.path.join(CURRENT_DIR, "..", "sam3"))
    
    if os.path.exists(sam3_path):
        try:
            # sys.executable ensures it installs inside the active virtual environment
            subprocess.run(
                [sys.executable, "-m", "pip", "install", "-e", sam3_path, "-i", "https://pypi.tuna.tsinghua.edu.cn/simple"],
                check=True
            )
            print("[✓] SAM3 modules successfully installed!\n")
            return True
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Failed to run pip installation for SAM3: {e}\n")
            return False
    else:
        print("[WARNING] Local 'sam3' folder was not found. Skipping SAM3 installation.\n")
        return False

def check_first_run_auth_and_setup():
    """
    Replicates your .bat installer logic.
    Only prompts and installs SAM3 if a HF token is successfully provided.
    """
    import huggingface_hub
    import importlib
    
    # 1. Check if they are already authenticated and have SAM3 installed
    try:
        if huggingface_hub.get_token():
            try:
                importlib.import_module("sam3")
                return  # SAM3 is present and authenticated, proceed silently.
            except ImportError:
                # Token exists but sam3 module needs to be installed.
                install_local_sam3()
                return
    except Exception:
        pass

    # 2. Prompt for token in the terminal if it is missing
    print("\n" + "=" * 65)
    print("           TAAM TRACKER - MODEL CONFIGURATION")
    print("=" * 65)
    print("To enable the SAM3 model, a Hugging Face Token is required.")
    print("If you skip this, only Ultralytics YOLO will be available.")
    print("-" * 65)
    
    try:
        token = input("Paste your Hugging Face Token (or press Enter to skip): ").strip()
        if token:
            print("\n[*] Authenticating with Hugging Face...")
            try:
                huggingface_hub.login(token=token)
                # Successful authentication -> install local sam3
                install_local_sam3()
            except Exception as e:
                print(f"[ERROR] Authentication failed: {e}")
                print("[INFO] SAM3 configuration skipped. YOLO-only mode active.")
        else:
            print("\n[INFO] No token provided. Skipping SAM3 installation...")
            print("[INFO] YOLO-only mode successfully configured.")
    except (KeyboardInterrupt, EOFError):
        print("\n[!] Setup skipped.")
    print("=" * 65 + "\n")


# --- UNIFIED ENTRY POINT ---

def main():
    # 1. Clean up PyQt6 DLL conflicts on Windows
    fix_windows_dll_path()
    
    # 2. Replicate .bat setup behavior conditionally
    check_first_run_auth_and_setup()
    
    # 3. Import and launch the PyQt6 Application Loop
    from PyQt6.QtWidgets import QApplication
    app = QApplication(sys.argv)
    
    # DEFERRED IMPORT: Importing the main window after QApplication initialization
    # prevents OpenGL and C++ graphics environment conflicts that cause native crashes.
    from gui.main_window import TAAMMainWindow
    
    window = TAAMMainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()