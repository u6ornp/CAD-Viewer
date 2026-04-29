# IGES Support Setup Guide

## Overview
The CAD Viewer now supports IGES file format with automatic conversion to STL for viewing. IGES files are converted server-side using the Open Cascade geometry kernel.

## Requirements

### System Requirements
- Python 3.7+
- Windows, macOS, or Linux
- ~500MB disk space for pythonocc installation

### Dependencies
The IGES reader requires:
- **pythonocc-core 7.7.2** - Open Cascade Python bindings for CAD geometry processing

## Installation

### Step 1: Install pythonocc-core

Run the installation script:

```bash
# On Windows (in command prompt or PowerShell)
pip install pythonocc-core==7.7.2

# On macOS/Linux
pip3 install pythonocc-core==7.7.2
```

**Note:** pythonocc-core is a large package (~100-200MB) and includes compiled Open Cascade libraries. Installation may take 2-5 minutes.

### Step 2: Verify Installation

Test that IGES support is working:

```bash
python -c "from iges_reader import check_pythonocc; print('IGES Support:', check_pythonocc())"
```

Expected output: `IGES Support: True`

### Step 3: Launch the Viewer

Run the server as normal:

```bash
# Windows
start.bat

# macOS/Linux
python3 server.py
```

The server will automatically detect IGES support and enable it.

## Usage

### Loading IGES Files

1. **Using the Open Button:**
   - Click the 📁 button
   - Select `.iges` or `.igs` files
   - The file will be converted to STL automatically
   - Progress shows: `⟳ Converting filename.iges to STL...`
   - Once loaded, displays: `✓ 1 part(s) loaded`

2. **Using Drag & Drop:**
   - Drag `.iges` or `.igs` files onto the viewport
   - Conversion starts automatically
   - View appears once complete

### Supported File Types

- **✅ .IGES** - Standard IGES format
- **✅ .IGS** - Alternate IGES extension
- **Full geometry support:** Solids, surfaces, curves, and assemblies

## How It Works

### Conversion Pipeline

```
┌─────────────────────┐
│  IGES File Upload   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────────────────────┐
│  Server: /convert-iges endpoint     │
│  - Receives IGES binary data        │
│  - Creates temporary file           │
└──────────┬──────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│  IGESConverter.convert_bytes()      │
│  - Uses Open Cascade kernel         │
│  - Reads IGES geometry              │
│  - Tessellates surfaces to mesh     │
│  - Outputs STL file                 │
└──────────┬──────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│  Server returns STL data            │
│  - Binary STL format (binary faster)│
│  - Cleaned up temporary files       │
└──────────┬──────────────────────────┘
           │
           ▼
┌─────────────────────────────────────┐
│  Browser: loadFile() processes STL  │
│  - Parses STL geometry              │
│  - Creates Three.js mesh            │
│  - Adds to scene                    │
└─────────────────────────────────────┘
```

## Troubleshooting

### "IGES support not available"

**Problem:** Server responds with 503 error and "IGES support not available"

**Solution:**
1. Install pythonocc-core: `pip install pythonocc-core==7.7.2`
2. Restart the server: `start.bat` or `python3 server.py`
3. Try converting again

### Installation fails with "wheel" error

**Problem:** `error: Microsoft Visual C++ 14.0 is required` (Windows)

**Solution:**
1. Install Microsoft C++ Build Tools: https://visualstudio.microsoft.com/downloads/
2. Or install Python from official python.org (includes build tools)
3. Retry: `pip install pythonocc-core==7.7.2`

### Conversion times out or hangs

**Problem:** Very large/complex IGES files take too long

**Solution:**
- Open Cascade is single-threaded
- Complex assemblies with many parts may take 30+ seconds
- Simplify IGES geometry in source CAD software before exporting
- Use "Export as STL" in your CAD software as an alternative

### "No valid geometry in IGES file"

**Problem:** Error: "IGES file contains no valid geometry"

**Solution:**
1. Verify IGES file is not corrupted
2. Try opening in FreeCAD or another CAD software to confirm
3. Re-export from source CAD application (check export settings)
4. Try converting with FreeCAD instead: `File → Export As STL`

## Technical Details

### Supported IGES Entities

Open Cascade supports most IGES entity types:
- **Solids:** Blocks, cylinders, spheres, swept solids, boolean operations
- **Surfaces:** NURBS, B-spline, ruled surfaces
- **Curves:** NURBS, B-spline, circles, lines, arcs
- **Assemblies:** Part instances, transformations, references

### Mesh Quality

The conversion process automatically:
- Detects optimal tessellation tolerance
- Generates triangular mesh from surfaces
- Preserves geometric accuracy
- Handles multi-part assemblies

### Performance

Typical conversion times:
- **Small parts** (< 100k triangles): < 2 seconds
- **Medium parts** (100k-1M triangles): 2-10 seconds
- **Large assemblies** (> 1M triangles): 10-60 seconds

## File Structure

```
CAD-analyser/
├── iges_reader/           # IGES conversion module
│   ├── __init__.py        # Module initialization
│   ├── converter.py       # IGESConverter class
│   └── requirements.txt   # pythonocc-core dependency
├── cad_viewer.html        # Updated UI with IGES support
├── server.py              # Updated server with /convert-iges endpoint
├── start.bat              # Launcher script
└── IGES_SETUP.md         # This file
```

## Limitations

- **Binary STEP files** (.stp) are not yet supported (future enhancement)
- **2D IGES drawings** are not converted (only 3D geometry)
- **Very large files** (> 10MB) may be slow or run out of memory
- **Parametric features** are not preserved (only static geometry)

## FAQ

**Q: Can I convert STEP files too?**
A: Not yet, but the architecture supports it. STEP conversion can be added with minimal changes.

**Q: Why does my IGES file look wrong after conversion?**
A: IGES geometry may not tessellate well with default settings. Try:
1. Re-export IGES from source CAD with higher precision
2. Use "Export as STL" directly from your CAD software
3. Simplify geometry before exporting

**Q: Can I disable IGES support?**
A: Yes, uninstall pythonocc-core: `pip uninstall pythonocc-core`
   The viewer will work normally with STL/OBJ only.

**Q: Is the IGES file uploaded to a server?**
A: No, conversion happens locally on your machine. Files never leave your computer.

## Support

For issues with:
- **pythonocc-core installation:** See https://github.com/tpaviot/pythonocc-core
- **CAD Viewer:** Report issues in the project repository
- **IGES file corruption:** Re-export from source CAD application

---

**Version:** 1.0.0  
**Last Updated:** 2026-04-29
