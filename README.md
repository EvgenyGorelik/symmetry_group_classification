# symmetry_group_classification

Determines the symmetry group of atoms in a cell

## 🌐 Web Application

This project includes a web-based frontend that runs Python in the browser using WebAssembly (Pyodide). No backend server required!

**Features:**
- 📤 Upload data files with atomic coordinates
- 💻 Real-time console output
- 🔬 Automatic symmetry analysis
- 🎨 Modern, responsive UI

### Try it Online

Once deployed to GitHub Pages, the application will be available at:
`https://[username].github.io/symmetry_group_classification/`

### Local Usage

Simply open `docs/index.html` in a modern web browser, or serve it with any static file server:

```bash
# Using Python
cd docs
python -m http.server 8000

# Using Node.js
npx serve docs

# Or just open the file directly
open docs/index.html
```

### Input Format

The application accepts atomic coordinates in various formats:
- Space-separated values (`.txt`)
- Comma-separated values (`.csv`)
- JSON format (`.json`)

See `docs/README.md` for detailed usage instructions and sample files.

## 📊 Symmetry Analysis

The tool analyzes structures for:
- Inversion symmetry
- Mirror planes (xy, xz, yz)
- Rotational symmetry (2-fold, 3-fold, 4-fold, 6-fold)
- Point group classification

## 🚀 Deployment

To deploy to GitHub Pages:

1. Go to repository Settings → Pages
2. Select "Deploy from a branch"
3. Choose `main` branch and `/docs` folder
4. Save and wait for deployment

## 📝 License

Open source project for symmetry group classification of atomic structures.
