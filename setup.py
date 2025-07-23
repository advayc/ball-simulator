from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ball-simulator",
    version="1.0.0",
    author="Advay Chandorkar",
    author_email="",
    description="Interactive Physics Ball Simulation with Multiple Visual Styles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/advayc/ball-simulator",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Topic :: Games/Entertainment :: Simulation",
        "Topic :: Scientific/Engineering :: Physics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pygame>=2.5.0",
        "pygbag>=0.9.0",
    ],
    entry_points={
        "console_scripts": [
            "ball-simulator=main:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/advayc/ball-simulator/issues",
        "Source": "https://github.com/advayc/ball-simulator",
        "Demo": "https://advayc.github.io/ball-simulator/",
    },
)
