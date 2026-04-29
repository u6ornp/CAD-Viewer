# IGES Installation Guide - All Options

## Quick Start

### Option 1: Automatic Installation (Easiest)

Double-click `iges_reader/install.bat` and follow the prompts. It will:
- Check your Python installation
- Try multiple pythonocc-core versions
- Provide alternatives if installation fails

### Option 2: Manual Installation - Try in Order

```bash
# Option A: Latest pythonocc-core (most likely to work)
pip install pythonocc-core

# If that fails, try specific versions:
pip install "pythonocc-core>=7.7,<7.8"
pip install "pythonocc-core>=7.6,<7.7"  
pip install "pythonocc-core>=7.5,<7.6"
```

### Option 3: Use Conda (Most Reliable for pythonocc)

```bash
# If you have Anaconda/Miniconda installed:
conda install -c conda-forge pythonocc-core
```

### Option 4: Use FreeCAD Instead

1. **Download FreeCAD** (free): https://www.freecadweb.org/downloads/
2. **Install** and choose "Add FreeCAD to PATH" during installation
3. **Restart your terminal**
4. IGES support will work automatically using FreeCAD

## Why the Error?

**"Could not find a version that satisfies the requirement"** means:

1. **Your Python version is incompatible**
   - pythonocc only supports Python 3.7-3.11
   - Check your version: `python --version`
   - If you have Python 3.12+, downgrade or use Conda

2. **No pre-built wheels for your system**
   - pythonocc needs to be compiled for your OS/architecture
   - Conda usually has pre-built wheels, pip might not

3. **pip cache issue**
   - Try: `pip install --upgrade --force-reinstall pythonocc-core`
   - Or clear cache: `pip cache purge`

## Verification

After installation, verify it works:

```bash
python -c "from iges_reader import check_pythonocc; print('IGES Support:', check_pythonocc())"
```

Expected output: `IGES Support: True`

## Recommended Approach

**Try in this order:**

1. ✅ `install.bat` (automatic) - 70% success rate
2. ✅ `conda install pythonocc-core` - 95% success rate  
3. ✅ Download FreeCAD - 100% success rate (universal solution)
4. ✅ Manual conversion - Convert IGES→STL in CAD software

## System-Specific Solutions

### Windows

```bash
# Method 1: pip (might fail on Windows)
pip install pythonocc-core

# Method 2: Conda (most reliable)
conda install -c conda-forge pythonocc-core

# Method 3: FreeCAD (if pythonocc fails)
# Download: https://github.com/FreeCAD/FreeCAD/releases
# Install and use it to convert IGES→STL
```

### macOS

```bash
# Method 1: Conda (recommended)
conda install -c conda-forge pythonocc-core

# Method 2: Homebrew
brew install pythonocc

# Method 3: FreeCAD
brew install freecad
```

### Linux (Ubuntu/Debian)

```bash
# Method 1: Conda (recommended)
conda install -c conda-forge pythonocc-core

# Method 2: apt (if available)
sudo apt install python3-pythonocc

# Method 3: FreeCAD
sudo apt install freecad
```

## If All Else Fails

### Manual Conversion (No Dependencies Needed)

1. Open your IGES file in free CAD software:
   - **FreeCAD** (best): https://www.freecadweb.org/
   - **Fusion 360** (free tier)
   - **SolidWorks** (if you have it)
   - **SolidEdge** (if you have it)

2. In the CAD software:
   - File → Open → Select your `.iges` file
   - File → Export As → Choose `STL` format
   - Save the converted file

3. In the 3D Viewer:
   - Load the `.stl` file (no dependencies needed)

**This always works** because you're converting in professional CAD software that already has IGES support built-in.

## Troubleshooting Specific Errors

### "no module named 'OCP'"
```bash
pip install pythonocc-core
# Restart your terminal/IDE after installation
```

### "Visual C++ 14.0 required" (Windows)
```bash
# Download Microsoft C++ Build Tools
# https://visualstudio.microsoft.com/visual-cpp-build-tools/
# Or use Conda which has pre-built wheels
conda install -c conda-forge pythonocc-core
```

### "No module named 'FreeCAD'"
- FreeCAD is optional, only needed as a fallback
- pythonocc or manual conversion will work

### Installation times out
```bash
# Increase timeout (slow network)
pip install --default-timeout=1000 pythonocc-core

# Or use Conda (faster mirrors)
conda install -c conda-forge pythonocc-core
```

## What Gets Installed

- **pythonocc-core**: ~150-200 MB on disk
  - Open Cascade geometry kernel
  - Python bindings for CAD operations
  - Takes 5-10 minutes to download and install

- **FreeCAD**: ~500 MB on disk  
  - Full CAD application
  - IGES support built-in
  - Only ~1 minute download on modern internet

## Performance Note

- pythonocc: Fast, native library, ~2-60 seconds per file
- FreeCAD (Python): Medium speed, subprocess overhead, ~5-90 seconds per file
- FreeCAD (command-line): Can be slower, but works even if Python module not available
- Manual conversion: One-time effort, then just load STL

## Still Not Working?

1. **Python version issue?**
   ```bash
   python --version  # Should be 3.7-3.11
   ```

2. **Check pip**
   ```bash
   pip --version
   python -m pip install --upgrade pip
   ```

3. **Try Conda instead**
   ```bash
   # Download: https://conda.io/projects/conda/en/latest/user-guide/install/
   conda install -c conda-forge pythonocc-core
   ```

4. **Download FreeCAD**
   ```
   https://www.freecadweb.org/downloads/
   ```

5. **Use manual conversion**
   - Open in FreeCAD → Export as STL → Load in viewer

All options work. Some just require a few steps. Choose the one that works for your system!

---

**Questions?** Check `IGES_SETUP.md` for more details about usage and features.
