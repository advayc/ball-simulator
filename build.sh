#!/bin/bash

# Ball Simulator Build Script
# This script builds the web version using pygbag

echo "🚀 Building Ball Simulator for web deployment..."

# Check if pygbag is installed
if ! command -v pygbag &> /dev/null; then
    echo "❌ pygbag not found. Installing..."
    pip install pygbag
fi

# Clean previous builds
if [ -d "build/web" ]; then
    echo "🧹 Cleaning previous build..."
    rm -rf build/web
fi
if [ -d "dist" ]; then
    rm -rf dist
fi

# Build with pygbag
echo "🔨 Building with pygbag..."
pygbag --build main.py

# Check if build was successful
if [ -d "build/web" ]; then
    echo "📁 Moving files to dist directory for deployment..."
    mv build/web dist
    echo "✅ Build successful! Web files are in the 'dist' directory."
    echo "📁 You can now deploy the 'dist' directory to any web server."
    echo "🌐 For GitHub Pages, the GitHub Action will handle deployment automatically."
else
    echo "❌ Build failed. Please check the output above for errors."
    exit 1
fi
