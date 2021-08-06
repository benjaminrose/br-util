"""sn.py - calculate a naive Tripp standard"""

from astropy.cosmology import wCDM


def tripp_standardize(
    mb,
    x1,
    c,
    z,
    M0=19.34,
    alpha=0.15,
    beta=3.1,
    cosmo={"H0": 70, "Om0": 0.3, "Ode0": 0.7, "w0": -1},
):
    """
    Arguments
    ---------
    mb:

    x1:

    c:

    z:

    M0:
        Defaults to 19.34.

    alpha:
        Defaults to 0.15.

    beta:
        Defaults to 3.1.

    cosmo: dictionary
        A dictionary passed to Astropy's wCDM,
        https://docs.astropy.org/en/stable/api/astropy.cosmology.wCDM.html.
        Defaults to `{'H0':70, 'Om0': 0.3, 'Ode0': 0.7, 'w0':=-1}'
    """
    COSMO = wCDM(**cosmo)
    mu = COSMO.distmod(z).value
    tripp = mb + M0 + alpha * x1 - beta * c - mu

    return tripp
