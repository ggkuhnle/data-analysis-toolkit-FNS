"""Plotting helpers wrapping Matplotlib/Seaborn."""
import matplotlib.pyplot as plt
import seaborn as sns

def hist_by_group(df, var, group_col, **kwargs):
    sns.histplot(data=df, x=var, hue=group_col, **kwargs)
    plt.show()

