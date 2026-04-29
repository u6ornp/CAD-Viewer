# Setup & Installation Guide

## Prerequisites

### System Requirements
- **Python:** 3.7 or higher
- **Operating System:** Windows, macOS, or Linux
- **Browser:** Chrome, Firefox, Safari, or Edge
- **Memory:** 512 MB minimum (2 GB recommended)
- **Disk Space:** 50 MB for application + space for your model files

## Installation Steps

### Step 1: Install Python

#### Windows
1. Download from https://www.python.org/downloads/
2. Run the installer
3. **IMPORTANT:** Check "Add Python to PATH" during installation
4. Click "Install Now"
5. Verify installation:
   ```bash
   python --version
   ```

#### macOS
```bash
# Using Homebrew (if installed)
brew install python3

# Or download from https://www.python.org/downloads/
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
```

### Step 2: Download the Project

**Option A: Git (Recommended)**
```bash
git clone https://github.com/yourusername/CAD-Viewer.git
cd CAD-Viewer
```

**Option B: Download ZIP**
1. Click "Code" → "Download ZIP"
2. Extract to desired location
3. Open terminal in extracted folder

### Step 3: Launch the Viewer

#### Windows
Double-click: `start.bat`

Or open Command Prompt:
```bash
python server.py
```

#### macOS/Linux
Open Terminal in the project folder:
```bash
python3 server.py
```

### Step 4: Access the Viewer

The browser should open automatically to:
```
http://localhost:8080
```

If not, manually open that URL in your browser.

## Optional Features

### IGES File Support

To enable IGES/IGS file viewing, install the IGES converter:

#### Option 1: pythonocc (Recommended)
```bash
pip install pythonocc-core
```

Takes 5-10 minutes to install (large package).

#### Option 2: FreeCAD
1. Download from https://www.freecadweb.org/
2. Install and select "Add to PATH"
3. Restart the server

See `IGES_SETUP.md` for detailed instructions.

## Troubleshooting

### "Python not found"
- **Windows:** Reinstall Python and ensure "Add to PATH" is checked
- **macOS/Linux:** Use `python3` instead of `python`

### "Port 8080 already in use"
**Option 1:** Kill existing process
```bash
# Windows
netstat -ano | findstr :8080
taskkill /PID [PID] /F

# macOS/Linux
lsof -i :8080
kill -9 [PID]
```

**Option 2:** Change port in `server.py`
```python
PORT = 8081  # Change to any available port
```

### Server starts but browser won't open
- Manually navigate to `http://localhost:8080`
- Check firewall settings
- Try a different browser

### "Module not found" errors
- Ensure you're in the project directory
- Reinstall Python
- Check that all files were extracted/downloaded

## Project Structure

```
CAD-Viewer/
├── README.md              # Project overview
├── SETUP.md               # This file
├── LICENSE                # MIT License
├── .gitignore             # Git configuration
├── cad_viewer.html        # Main application
├── server.py              # Web server
├── start.bat              # Windows launcher
├── requirements.txt       # Optional dependencies
├── test-cube.stl          # Example file
├── HOW_TO_USE.txt         # User guide
└── iges_reader/           # Optional IGES support
```

## Configuration

### Changing the Server Port
Edit `server.py`:
```python
PORT = 8080  # Change this number
```

### Disabling Auto-Browser Open
In `server.py`, comment out:
```python
# Timer(1.0, open_browser).start()
```

## Network Access

### Access from Another Computer on Same Network
1. Get your IP address:
   - **Windows:** `ipconfig` (look for IPv4 Address)
   - **macOS/Linux:** `ifconfig` (look for inet)

2. Share: `http://[your-ip]:8080`

### Internet Hosting
For public access, deploy to:
- **Heroku** (free tier available)
- **AWS** (free tier available)
- **Azure** (free tier available)
- **Vercel** (frontend only)
- **Replit** (simple Python hosting)

## Verification

After starting, verify everything works:
1. Open browser to `http://localhost:8080`
2. Click 📁 button
3. Select `test-cube.stl` (included in project)
4. Model should display as a cube
5. Rotate with mouse to verify controls work

## Getting Help

### Common Issues
- See `HOW_TO_USE.txt` for feature questions
- Check `IGES_SETUP.md` if IGES support needed
- Review this file for installation issues

### Performance Issues
- Close other applications
- Disable edge display for large files
- Use smaller model files for testing
- Check available disk space

## Next Steps

Once installed:
1. Review `README.md` for feature overview
2. Read `HOW_TO_USE.txt` for usage instructions
3. Load your own STL/OBJ files
4. Explore advanced features (selection, cuts, etc.)

## System Information

Run this command to check your setup:

```bash
# Windows
python --version
pip --version

# macOS/Linux
python3 --version
pip3 --version
```

Expected output:
```
Python 3.9.0 (or higher)
pip 21.0.0 (or higher)
```

---

**Setup Version:** 1.0.0  
**Last Updated:** 2026-04-29
