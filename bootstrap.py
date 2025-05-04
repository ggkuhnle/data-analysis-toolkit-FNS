#!/usr/bin/env python
"""
bootstrap.py – environment setup

Installs requirements and the toolkit in editable mode.
"""
from pathlib import Path
import subprocess, sys

ROOT = Path(__file__).resolve().parent
REQ = ROOT / "requirements.txt"

print("🔧 Installing requirements…")
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", str(REQ)])
print("🔧 Installing toolkit editable…")
subprocess.check_call([sys.executable, "-m", "pip", "install", "-e", str(ROOT)])
print("✅ Environment ready!")

