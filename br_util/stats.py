"""stats.py"""


def robust_scatter(x):
    "aka converting from MAD to sigma equivalent"
    return 1.4826 * np.median(np.abs(x - np.median(x)))


def p2sigma():
    pass
