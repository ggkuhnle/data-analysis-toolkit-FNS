"""
datasets.py – load or download small example datasets
"""

import pandas as pd
from pathlib import Path

def get_dataset(name: str) -> pd.DataFrame:
    """
    Return a DataFrame for a given bundled dataset name.
    Looks first in package resources, then in top-level data/ if not found.
    """
    pkg_path = Path(__file__).parent / "_resources" / f"{name}.csv"
    if pkg_path.exists():
        return pd.read_csv(pkg_path)

    local_path = Path(__file__).resolve().parent.parent / "data" / f"{name}.csv"
    if local_path.exists():
        return pd.read_csv(local_path)

    raise FileNotFoundError(
        f"Dataset '{name}' not found in package resources or data/ folder."
    )

