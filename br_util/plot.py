"""plot.py
"""

from pathlib import Path

import matplotlib.pyplot as plt


def save_plot(filename, save):
    if save:
        folder = Path("figures/")
        folder.mkdir(exist_ok=True)
        plt.savefig(folder / filename, bbox_inches="tight")
    else:
        plt.show()
