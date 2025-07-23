#!/bin/bash

# Install required packages
echo "Installing required packages..."
pip install pygame pygbag

# Test locally
echo "Starting local test server..."
echo "Visit http://localhost:8000 in your browser"
echo "Press Ctrl+C to stop the server when done testing"
pygbag --port 8000 --width 800 --height 600 main.py

# Build for web deployment
echo "Building for web deployment..."
pygbag --build --ume_block 0 --width 800 --height 600 main.py

echo ""
echo "Build complete! The web version is in the build/web directory."
echo "To deploy to GitHub Pages:"
echo "1. Create a gh-pages branch in your repo"
echo "2. Copy contents of build/web to the gh-pages branch"
echo "3. Push to GitHub"
echo ""
echo "Your simulator will be available at: https://[username].github.io/[repo-name]/"
