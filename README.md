# CAD Viewer

A browser-based 3D CAD file viewer for STL and OBJ files with advanced features like face selection, mesh manipulation, and part management.

## ✨ Features

### File Support
- **STL files** - Load directly (binary and ASCII formats)
- **OBJ files** - Full support
- **IGES files** - Optional support (requires pythonocc-core)
- **Drag & Drop** - Load files by dragging onto the viewport

### 3D Visualization
- **Interactive 3D Viewport** - Rotate, pan, zoom with mouse
- **Multi-Part Support** - Load and view multiple files simultaneously
- **Color Management** - Individual color control for each part
- **Edge Display** - Toggle edge outlines with custom colors
- **Grid Visualization** - Optional grid background
- **Lighting** - Multi-light system with consistent illumination
- **Orientation Triad** - 3D axes indicator in bottom-left

### Advanced Features
- **Face Selection** - Multiple selection modes:
  - Single: Select individual triangles
  - Add: Accumulate selections
  - Connected: Flood-fill to adjacent faces
  - By Angle: Select faces with similar normals
- **Section Cuts** - Cut along X, Y, Z axes with visual preview
- **Part Extraction** - Create new parts from selected faces
- **Part Tree** - Sidebar with visibility toggles and color indicators

### Controls
```
Left Mouse + Drag    → Rotate view
Right Mouse + Drag   → Pan view
Scroll Wheel         → Zoom in/out
📁 Button           → Open files
↔ Button            → Fit all to view
```

## 🚀 Quick Start

### Requirements
- Python 3.7+
- Modern web browser (Chrome, Firefox, Safari, Edge)
- No external dependencies required for basic STL/OBJ viewing

### Installation & Launch

1. **Clone/Download this repository**
   ```bash
   git clone https://github.com/yourusername/CAD-Viewer.git
   cd CAD-Viewer
   ```

2. **Run the server**
   
   **Windows:**
   ```bash
   start.bat
   ```
   
   **macOS/Linux:**
   ```bash
   python3 server.py
   ```
   
   The viewer will automatically open in your default browser at `http://localhost:8080`

3. **Load a file**
   - Click 📁 to browse and select an STL or OBJ file
   - Or drag & drop files onto the viewport

## 📋 Usage Guide

### Basic Workflow
1. Open an STL/OBJ file using the 📁 button
2. Use mouse to rotate (left-click + drag), pan (right-click), and zoom (scroll)
3. Use the toolbar at the bottom for additional controls

### Selecting Faces
1. Choose a selection mode from the bottom toolbar
2. Click on faces to select them
3. Selected faces highlight in yellow
4. Use ⊗ to clear selection

### Creating Parts from Selection
1. Select faces using any selection mode
2. Click ✦ Create Part button
3. Enter a custom color (hex format, e.g., #FF0000)
4. New part appears in the sidebar

### Working with Multiple Files
1. Open first file - it appears with a default color
2. Click ↔ to fit it to view
3. Open additional files - each gets a different color
4. Click on parts in the sidebar to select/manage them
5. Use color picker to change individual part colors

### Section Cuts
1. Click X, Y, or Z to cut along that axis
2. The cut plane passes through the model center
3. Click ✕ to clear the cut

## 📁 Project Structure

```
CAD-Viewer/
├── README.md                 # This file
├── SETUP.md                  # Detailed setup instructions
├── HOW_TO_USE.txt            # User guide
├── LICENSE                   # MIT License
├── .gitignore                # Git ignore rules
├── cad_viewer.html           # Main application (all-in-one file)
├── server.py                 # Python HTTP server
├── start.bat                 # Windows launcher
├── requirements.txt          # Optional dependencies
├── test-cube.stl             # Example STL file
├── IGES_OPTIONS.txt          # IGES support options (optional)
├── IGES_SETUP.md             # IGES setup guide (optional)
├── IGES_INSTALL.md           # IGES installation (optional)
└── iges_reader/              # IGES support module (optional)
    ├── __init__.py
    ├── converter.py
    ├── freecad_converter.py
    ├── requirements.txt
    └── install.bat
```

## 🎯 System Requirements

### Minimum
- **OS:** Windows 7+, macOS 10.12+, Linux (any modern distribution)
- **Python:** 3.7 or higher
- **Browser:** Chrome, Firefox, Safari, Edge (any recent version)
- **RAM:** 512 MB
- **Disk:** 50 MB

### Recommended
- **Python:** 3.9 or higher
- **Browser:** Chrome or Edge (best performance)
- **RAM:** 2+ GB (for large models)

## 🔧 Optional Features

### IGES File Support
To enable IGES file conversion, install pythonocc-core:

```bash
pip install pythonocc-core
```

Or use FreeCAD:
1. Download from https://www.freecadweb.org/
2. Install and add to PATH
3. Restart the server

See `IGES_SETUP.md` for detailed instructions.

## 🖥️ Server Configuration

### Change Port
Edit `server.py` and modify:
```python
PORT = 8080  # Change to desired port
```

### Disable Browser Auto-Open
Comment out the timer in `server.py`:
```python
# Timer(1.0, open_browser).start()
```

## 📊 File Format Support

### STL (Stereolithography)
- ✅ Binary format
- ✅ ASCII format
- ✅ Multiple solid objects

### OBJ (Wavefront)
- ✅ Vertices and faces
- ✅ Normals
- ✅ Material colors

### IGES (optional)
- ✅ 2D/3D CAD models
- ✅ Surfaces and solids
- ✅ Assembly structures
- Requires: pythonocc-core or FreeCAD

## 🐛 Troubleshooting

### Server won't start
**Issue:** "Python not found"
- **Solution:** Install Python from https://www.python.org/
- Add Python to PATH during installation

### Port already in use
**Issue:** "Address already in use"
- **Solution:** Change PORT in server.py or kill existing process

### Browser won't open
**Issue:** Manual navigation needed
- **Solution:** Open `http://localhost:8080` in your browser

### File loads but shows nothing
**Issue:** Model is very large or very small
- **Solution:** Click ↔ (Fit) button to auto-zoom to contents

### Dark appearance
**Issue:** Poor lighting
- **Solution:** Model lighting adjusted; if still dark, try different browser

## 📦 Deployment

### Local Network
1. Get your machine's IP: `ipconfig` (Windows) or `ifconfig` (macOS/Linux)
2. Others can access: `http://[your-ip]:8080`

### Internet Hosting
1. Use cloud service (AWS, Azure, Heroku, etc.)
2. Deploy with: `python server.py`
3. Ensure port forwarding if behind firewall

### Docker (Optional)
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
EXPOSE 8080
CMD ["python", "server.py"]
```

## 📝 Performance Notes

**File Size Limits:**
- STL files: Up to ~100 MB (depends on system RAM)
- OBJ files: Up to ~50 MB
- Multiple files: 500 MB+ total workable

**Performance Tips:**
- Use binary STL (faster than ASCII)
- Close unused files
- Reduce browser tab count
- Disable edge display for large models

## 🎓 Example Usage

```
# Windows
start.bat

# macOS/Linux  
python3 server.py

# Open http://localhost:8080 in browser
# Load your STL file
# Rotate with mouse, zoom with scroll
```

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions welcome! Areas for enhancement:
- Additional file formats (STEP, Parasolid, etc.)
- Mesh editing features
- Measurement tools
- Color schemes/themes
- Performance optimizations

## 📞 Support

For issues or feature requests:
1. Check `HOW_TO_USE.txt` for common solutions
2. Review `SETUP.md` for setup issues
3. Open an issue on GitHub

## 🎉 Credits

Built with:
- **Three.js** - 3D graphics library
- **Python** - Web server
- **STL Parser** - Custom implementation

---

**Version:** 1.0.0  
**Last Updated:** 2026-04-29  
**Status:** Production Ready
