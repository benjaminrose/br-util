from typing import List, Tuple

import click

from br_util.stats import p2sigma as stats_p2sigma
from br_util import __version__

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.version_option(
    __version__, message="%(prog)s (part of br-util), version %(version)s"
)
@click.option(
    "--1",
    "tails",
    flag_value=1,
    default=True,
    help="Calculate sigma for a one-tail p-value (Default)",
)
@click.option(
    "--2", "tails", flag_value=2, help="Calculate sigma for a two-tail p-value"
)
@click.argument("p_value", required=True, type=float, nargs=-1)
def p2sigma(p_value: Tuple[float], tails: int = 1) -> List[float]:
    """Convert p-values to there corresponding sigma. Part of br-util"""
    # click returns variatic arguments (nargs=-1) as tuples
    sigmas = stats_p2sigma(p_value, tails)
    for sigma in sigmas:
        click.echo(f"{sigma:.2f}")
