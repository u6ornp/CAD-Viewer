# Selection Modes - Testing Guide

## Overview
The CAD Viewer now supports four distinct face selection modes for advanced geometry analysis and part extraction.

## Selection Modes

### 1. **Single** (⊙ Single)
- **Default mode**
- Click on any face to select ONLY that triangle
- Previous selection is cleared
- Use this for precise, individual face selection
- Great for: examining specific faces, extracting single features

### 2. **Add** (⊕ Add)
- Accumulate selections by clicking multiple faces
- Each click adds the clicked triangle to your selection (if not already selected)
- Use Ctrl+Click for quick mode switching
- The "Create Part" button shows total selected faces: `Added triangle X (N total)`
- Great for: building complex selections, combining non-adjacent faces

### 3. **Connected** (⊡ Connected)
- Click a face, automatically selects ALL connected faces
- "Connected" means sharing an edge with the originally clicked face (flood-fill algorithm)
- Selects the entire face region/patch in one click
- Example: Click one face of a cube → selects all 4 top faces if they share edges
- Great for: selecting entire surface patches, analyzing continuous regions

### 4. **By Angle** (⚡ By Angle)
- Click a face, selects all faces with SIMILAR normal directions
- Default threshold: 30 degrees from the clicked face's normal
- Captures all faces pointing in roughly the same direction
- Also includes opposite-facing surfaces (180° angle)
- Great for: selecting all "flat" surfaces, grouping similar-orientation faces

## Testing with test-cube.stl

The included `test-cube.stl` is a simple unit cube (1×1×1) with 12 triangles (2 per face).

### Expected Behavior:

**Single Mode:**
- Click top-left triangle → selects 1 face
- Click top-right triangle → clears previous, selects 1 new face

**Add Mode:**
- Click top-left triangle → selects 1
- Click top-right triangle → selects 2 total (both top faces)
- Click bottom face → selects 3 total

**Connected Mode:**
- Click any triangle on top face → should select both triangles (they share an edge)
- Click cube center → might select 4-6 connected triangles depending on mesh topology

**By Angle Mode:**
- Click top face triangle → selects both top face triangles (same normal: 0,0,1)
- Click side face triangle → selects both side triangles (same normal: e.g., 1,0,0)
- Might also select opposite faces if angle threshold matches

## Features

✅ **Real-time Visual Feedback**: Selected faces are highlighted in yellow (0xffff00)
✅ **Face Counter**: Info bar shows `Selected N triangle(s)...`
✅ **Create Part**: Extract selected faces into a new named part with custom color
✅ **Clear Selection**: ⊗ Clear button resets all selections

## Technical Details

- **Connected Algorithm**: BFS (breadth-first search) through edge adjacency map
- **Angle Algorithm**: Dot product of face normals (supports 0-30° and 150-180°)
- **STL Geometry**: Each triangle = 3 position attributes, no indexed faces
- **World Space**: All calculations use mesh.matrixWorld for accurate transforms

## Tips

1. **Performance**: On very large STL files (100k+ triangles), "Connected" and "By Angle" modes may be slightly slower due to geometry processing
2. **Edge Cases**: Very small angle threshold might select only the clicked face; increase to 45° or 60° for broader selection
3. **Multi-Part**: If multiple parts are loaded, selection works on the part you clicked
4. **Persistence**: Use "⊗ Clear" to reset selections before trying a different mode
