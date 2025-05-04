from importlib import metadata as _md
__version__ = _md.version("data-analysis-toolkit-fns")

from .datasets import get_dataset
from .cleaning import snake_case_columns
from .viz import hist_by_group
from .stats import table1, t_test
from .bayes import bayesian_logistic

__all__ = [
    "get_dataset", "snake_case_columns",
    "hist_by_group", "table1", "t_test",
    "bayesian_logistic", "__version__"
]

