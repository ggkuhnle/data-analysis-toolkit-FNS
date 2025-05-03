from importlib import metadata as _md
__version__ = _md.version(__name__)

from .datasets import get_dataset
from .cleaning import snake_case_columns, fill_missing
from .stats import anova, cohens_d
# …and so on
__all__ = [
    "get_dataset",
    "snake_case_columns",
    "fill_missing",
    "anova",
    "cohens_d",
    # …
]

