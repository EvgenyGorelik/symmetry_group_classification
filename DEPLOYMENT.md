# GitHub Pages Deployment Guide

This guide will help you deploy the Symmetry Group Classification web application to GitHub Pages.

## Option 1: Manual Deployment (Recommended for first-time setup)

### Step 1: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on **Settings** tab
3. In the left sidebar, click **Pages**
4. Under "Build and deployment":
   - Source: Select **Deploy from a branch**
   - Branch: Select **main** (or your default branch)
   - Folder: Select **/docs**
   - Click **Save**

### Step 2: Wait for Deployment

- GitHub will automatically build and deploy your site
- This usually takes 1-2 minutes
- You'll see a green checkmark when deployment is complete
- Your site will be available at: `https://[username].github.io/symmetry_group_classification/`

### Step 3: Verify Deployment

1. Click the "Visit site" button in the Pages settings
2. Wait for Pyodide to initialize (takes a few seconds on first load)
3. Upload one of the sample files to test functionality

## Option 2: Automated Deployment with GitHub Actions

If you want automatic deployments on every push:

### Step 1: Configure GitHub Pages for Actions

1. Go to repository **Settings** → **Pages**
2. Under "Build and deployment":
   - Source: Select **GitHub Actions**

### Step 2: Commit the Workflow File

The workflow file is already included at `.github/workflows/pages.yml`

### Step 3: Verify Workflow

1. Go to the **Actions** tab in your repository
2. You should see "Deploy GitHub Pages" workflow
3. It will run automatically on every push to the main branch
4. Or you can trigger it manually using the "Run workflow" button

## Troubleshooting

### Site not loading?

- Wait a few minutes - GitHub Pages can take time to deploy
- Check the Actions tab for deployment status
- Ensure the `docs/` folder is committed and pushed

### Python not initializing?

- Check your browser console for errors
- Try a different browser (Chrome/Firefox recommended)
- Check if Pyodide CDN is accessible from your network
- Clear browser cache and reload

### File upload not working?

- Ensure Python environment has initialized (status should show green)
- Check that your file format is supported (.txt, .csv, .json, .xyz)
- View console output for error messages

## Custom Domain (Optional)

To use a custom domain:

1. Add a file named `CNAME` in the `docs/` folder
2. Content should be your domain name (e.g., `symmetry.example.com`)
3. Configure DNS settings with your domain provider
4. Point A record to GitHub Pages IPs or CNAME to `[username].github.io`

## Local Development

To test locally before deploying:

```bash
# Using Python
cd docs
python -m http.server 8000
# Open http://localhost:8000 in browser

# Using Node.js
npx serve docs
# Open http://localhost:3000 in browser
```

## Browser Compatibility

✅ **Supported:**
- Chrome 90+
- Firefox 90+
- Safari 14+
- Edge 90+

❌ **Not Supported:**
- Internet Explorer
- Very old browser versions

## Security Notes

- All processing happens in the browser (client-side)
- No data is sent to any server
- Files are processed locally using WebAssembly
- Safe to use with sensitive data

## Performance Tips

- First load takes longer (~10-20 seconds) to download Pyodide
- Subsequent loads are faster due to browser caching
- Large files (>1MB) may take longer to process
- Use modern browsers for best performance

## Need Help?

If you encounter issues:
1. Check the browser console (F12) for error messages
2. Verify GitHub Pages is enabled in repository settings
3. Ensure all files in `docs/` folder are committed
4. Try the sample files first to verify functionality

## Updates

To update the deployed site:
1. Make changes to files in the `docs/` folder
2. Commit and push to the main branch
3. GitHub Pages will automatically rebuild (takes 1-2 minutes)
