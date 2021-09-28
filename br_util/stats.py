"""stats.py"""
from typing import List, Tuple

import numpy as np
from scipy.special import erfcinv


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


def p2sigma(p_value: Tuple[float], tails: int = 1) -> List[float]:
    """Convert p-values to there corresponding sigma. Part of the clistats toolkit."""
    # click returns variatic arguments (nargs=-1) as tuples
    p_value = np.array(p_value)
    sigmas = np.sqrt(2) * erfcinv(p_value * 2 / tails)
    return sigmas
