"""stats.py"""

import numpy as np


def robust_scatter(x):
    """aka MAD but converted to sigma equivalent.

    1.4826 * median(|x - median(x)|)

    Parameters
    ----------
    x: array_like
        Data vector to calculated scatter of

    Returns
    -------
    float
    """
    return 1.4826 * np.median(np.abs(x - np.median(x)))


def p2sigma():
    pass
