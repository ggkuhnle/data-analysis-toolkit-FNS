"""Statistical summary and test wrappers."""
import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency

def table1(df: pd.DataFrame, group_col: str,
           numeric_cols: list[str], cat_cols: list[str]) -> pd.DataFrame:
    # copy your create_table1_clean implementation here
    pass

def t_test(df, var, group_col):
    # implement or call SciPy’s ttest_ind
    pass

