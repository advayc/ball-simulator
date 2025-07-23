# Deployment Guide for Ball Simulator

This guide explains how to deploy the Ball Simulator to various platforms.

## 🌐 Web Deployment (GitHub Pages) - Recommended

The easiest way to deploy is using GitHub Pages with the automated GitHub Action:

### Automatic Deployment (GitHub Actions)

1. **Push to GitHub**: Simply push your changes to the `main` branch
2. **Enable GitHub Pages**: 
   - Go to your repository settings
   - Navigate to "Pages" section
   - Set source to "GitHub Actions"
3. **Done!** The action will automatically build and deploy your simulator

### Manual Web Build

If you want to build manually:

```bash
# Make sure you have pygbag installed
pip install pygbag

# Run the build script
./build.sh

# Or build manually
pygbag --build --ume_block 0 --cdn "https://pygame-web.github.io/archives/0.9/" --name "Ball Simulator" --icon favicon.ico main.py
```

The web build will be in the `dist` directory, which you can upload to any web server.

## 📦 Package Distribution

### PyPI Package

To create a distributable package:

```bash
# Install build tools
pip install build twine

# Build the package
python -m build

# Upload to PyPI (requires account)
python -m twine upload dist/*
```

### Executable

For a standalone executable:

```bash
# Install PyInstaller
pip install pyinstaller

# Create executable
pyinstaller --onefile --windowed main.py
```

## 🚀 Other Deployment Options

### Local Server
```bash
# Simple HTTP server for testing
python -m http.server 8000 -d dist
```

### Netlify/Vercel
Simply drag and drop the `dist` folder to these platforms.

### Your Own Server
Upload the contents of the `dist` directory to your web server.

## 📱 Mobile App (Android)

The simulator can also be packaged as an Android app using pygame-web tools, but web deployment is recommended for broader compatibility.

## 🔧 Troubleshooting

- **Build fails**: Ensure pygame and pygbag are properly installed
- **Web version doesn't load**: Check that all files in `dist` are uploaded
- **Performance issues**: The web version may be slower than native Python

## 🎯 Best Practices

1. Use the automated GitHub Actions for continuous deployment
2. Test locally before deploying
3. Keep the web version simple for best performance
4. Use the provided favicon.ico for branding
