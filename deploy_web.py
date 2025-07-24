#!/usr/bin/env python3
"""
Web deployment script for Ball Simulator using pygbag
"""
import asyncio
import sys
import os

def check_pygbag():
    """Check if pygbag is installed"""
    try:
        import pygbag
        print("✅ pygbag is installed")
        return True
    except ImportError:
        print("❌ pygbag not found. Installing...")
        return False

def install_dependencies():
    """Install required dependencies"""
    import subprocess
    
    try:
        # Install pygbag and pygame-ce
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pygbag", "pygame-ce"])
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install dependencies: {e}")
        return False

def build_for_web():
    """Build the project for web using pygbag"""
    import subprocess
    
    # Change to the project directory
    project_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_dir)
    
    try:
        # Build with pygbag
        cmd = [
            sys.executable, "-m", "pygbag",
            "--build",
            "--width", "800",
            "--height", "600", 
            "--app_name", "Ball_Simulator",
            "--icon", "assets/ball.png" if os.path.exists("assets/ball.png") else None,
            "--html", "index.html",
            "--ume_block", "0",
            "main.py"
        ]
        
        # Remove None values from command
        cmd = [item for item in cmd if item is not None]
        
        print("🚀 Building for web...")
        print(f"Running: {' '.join(cmd)}")
        
        subprocess.check_call(cmd)
        print("✅ Web build completed successfully!")
        print("📁 Output files are in the 'build/web/' directory")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed: {e}")
        return False

def main():
    """Main deployment function"""
    print("🌐 Ball Simulator Web Deployment")
    print("=" * 40)
    
    # Check and install dependencies
    if not check_pygbag():
        if not install_dependencies():
            sys.exit(1)
    
    # Build for web
    if build_for_web():
        print("\n🎉 Deployment successful!")
        print("📖 Instructions:")
        print("   1. Upload the 'build/web/' folder contents to your web server")
        print("   2. Or use GitHub Pages by committing to gh-pages branch")
        print("   3. Access via your web URL")
    else:
        print("\n❌ Deployment failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
