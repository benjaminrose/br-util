"""plot.py
"""

from pathlib import Path

import matplotlib.pyplot as plt


def new_figure(**kward):
    """
    passes all keyword arguments to `matplotlib.pyplot.subplots()`.

    Returns:
    -------
    fig

    ax
    """
    return plt.subplots(tight_layout=True, **kward)


def save_plot(filename=""):
    if filename:
        folder = Path("figures/")
        folder.mkdir(exist_ok=True)
        plt.savefig(folder / filename, bbox_inches="tight")
    else:
        plt.show()
