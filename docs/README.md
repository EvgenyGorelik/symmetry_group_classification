# Symmetry Group Classification Web Application

This is a web-based tool for determining the symmetry group of atoms in a cell. It uses Python (via Pyodide) running directly in your browser.

## Features

- 🌐 **No Backend Required**: Runs entirely in your browser using WebAssembly
- 📤 **File Upload**: Upload data files with atomic coordinates
- 💻 **Live Console**: Real-time output and results display
- 🔬 **Symmetry Analysis**: Automatic detection of:
  - Inversion symmetry
  - Mirror planes
  - Rotational symmetry (2-fold, 3-fold, 4-fold, 6-fold)
  - Point group classification

## Usage

1. **Wait for Initialization**: When you first load the page, Python will initialize (takes a few seconds)
2. **Upload File**: Click "Choose File" and select a data file with atomic coordinates
3. **Process**: Click "Process File" to run the symmetry analysis
4. **View Results**: See the analysis results in the console output

## Input File Format

The application accepts several formats:

### Space/Comma Separated (CSV/TXT)
```
# Comments start with #
1.0 1.0 0.0
-1.0 1.0 0.0
-1.0 -1.0 0.0
1.0 -1.0 0.0
```

### JSON Format
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

## Sample Files

Try these sample files included in the repository:
- `sample_square.txt` - Square planar arrangement (D4h symmetry)
- `sample_triangle.txt` - Triangular arrangement (D3h symmetry)
- `sample_cube.txt` - Cubic arrangement (high symmetry)

## Symmetry Groups Detected

The tool can identify various point groups including:
- **C₁**: No symmetry
- **Cₛ**: Single mirror plane
- **Cᵢ**: Inversion center
- **Cₙ**: n-fold rotation (n = 2, 3, 4, 6)
- **C₂ᵥ**: 2-fold with mirrors
- **Dₙ**: n-fold rotation with perpendicular 2-fold axes
- **Dₙₕ**: Dₙ with horizontal mirror plane
- **Kₕ**: Spherical symmetry (single atom)

## Technical Details

- **Frontend**: HTML5, CSS3, JavaScript
- **Python Runtime**: Pyodide (Python 3.11 in WebAssembly)
- **Libraries**: NumPy for numerical computations
- **Hosting**: GitHub Pages (static hosting)

## GitHub Pages Deployment

To deploy this application:

1. Push the `docs/` folder to your repository
2. Go to repository Settings → Pages
3. Select "Deploy from a branch"
4. Choose `main` branch and `/docs` folder
5. Save and wait for deployment

The site will be available at: `https://[username].github.io/[repository-name]/`

## Browser Compatibility

- ✅ Chrome/Edge (recommended)
- ✅ Firefox
- ✅ Safari 14+
- ❌ Internet Explorer (not supported)

## License

This project is part of the symmetry_group_classification repository.
