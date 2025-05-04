#!/usr/bin/env python
"""
setup.py – pure setuptools installer (v2.0.0)

This version removes the inline bootstrap logic so that `pip install -e .`
will not invoke pip in a subprocess during the build.  Environment
bootstrapping is now handled by a separate `bootstrap.py` script.
"""

from setuptools import setup, find_packages
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REQ_FILE = ROOT / "requirements.txt"

# Load install requirements from requirements.txt
def _load_reqs(path):
    return [
        line.strip()
        for line in Path(path).read_text().splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]

install_requires = _load_reqs(REQ_FILE)
README = (ROOT / "README.md").read_text()

setup(
    name="data-analysis-toolkit-fns",
    version="2.0.0",
    description="Teaching toolkit for Food & Nutrition Science data analysis",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Gunter Academic",
    python_requires=">=3.9",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=install_requires,
    extras_require={
        "dev": [
            "black",
            "ruff",
            "pytest",
            "nbqa",
            "jupyter",
            "ipykernel",
            "quarto-cli",
        ],
    },
    entry_points={
        "console_scripts": [
            "fns-download-data=fns_toolkit.cli:download_data",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Education",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
)

