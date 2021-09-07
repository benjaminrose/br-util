import pytest
import numpy as np

from br_util import sn


class TestTrippStandardize:
    def test_tripp(self):
        assert sn.tripp_standardize(-19, 0, 0, 0.001) == pytest.approx(-27.82, 1e-4)

    def test_redshift_zero(self):
        assert sn.tripp_standardize(-19, 0, 0, 0.0) == np.inf
