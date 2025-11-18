# Quick Start Guide

## For Users: Using the Web Application

1. **Access the Application**
   - Visit: `https://[username].github.io/symmetry_group_classification/`
   - Wait 5-10 seconds for Python to initialize

2. **Upload Your Data**
   - Click "Choose File" button
   - Select a file with atomic coordinates (.txt, .csv, .json)
   - Click "Process File"

3. **View Results**
   - See analysis in the console output
   - Results include:
     - Number of atoms
     - Center of mass
     - Symmetry elements detected
     - **Point group classification**

## For Developers: Local Testing

```bash
# Clone the repository
git clone https://github.com/EvgenyGorelik/symmetry_group_classification.git
cd symmetry_group_classification

# Serve locally
cd docs
python -m http.server 8000

# Open in browser
# Navigate to: http://localhost:8000
```

## Sample Data

Try these included examples:
- **sample_square.txt** - Square planar (D₄ₕ symmetry)
- **sample_triangle.txt** - Triangular (D₃ₕ symmetry)  
- **sample_cube.txt** - Cubic (high symmetry)

## Input Format Examples

### Space-separated (TXT)
```
1.0 1.0 0.0
-1.0 1.0 0.0
-1.0 -1.0 0.0
1.0 -1.0 0.0
```

### Comma-separated (CSV)
```
1.0, 1.0, 0.0
-1.0, 1.0, 0.0
-1.0, -1.0, 0.0
1.0, -1.0, 0.0
```

### JSON
```json
{
  "atoms": [
    [1.0, 1.0, 0.0],
    [-1.0, 1.0, 0.0],
    [-1.0, -1.0, 0.0],
    [1.0, -1.0, 0.0]
  ]
}
```

## What Gets Analyzed

The tool examines your atomic structure for:

1. **Inversion Symmetry** - Does the structure have a center of inversion?
2. **Mirror Planes** - Are there xy, xz, or yz reflection planes?
3. **Rotational Symmetry** - Does it have 2-fold, 3-fold, 4-fold, or 6-fold rotation axes?
4. **Point Group** - What is the overall symmetry classification?

## Example Output

```
============================================================
SYMMETRY GROUP CLASSIFICATION RESULTS
============================================================

Number of atoms: 4

Center of mass:
  [0.0, 0.0, 0.0]

Inversion symmetry: Yes

Mirror planes: xy, xz, yz

Rotational symmetry: 4-fold, 2-fold

============================================================
SYMMETRY GROUP: D_4h (tetragonal)
============================================================
```

## Troubleshooting

**Page not loading?**
- Check if you're using a modern browser (Chrome, Firefox, Safari 14+)
- Disable ad blockers that might block the Pyodide CDN

**Python initialization slow?**
- First load downloads ~20MB of Python runtime
- Subsequent loads are faster due to caching
- This is normal and expected

**File not processing?**
- Ensure Python has initialized (green status)
- Check file format matches examples
- Look for error messages in console

## Need Help?

See the full documentation:
- `docs/README.md` - Detailed usage guide
- `DEPLOYMENT.md` - Deployment instructions
- Repository issues - Report bugs or ask questions
