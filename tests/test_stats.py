import pytest
from br_util import stats


class TestRobustScatter:
    def test_scatter(self):
        """Test a specific known case."""
        x = [2, 3, 1, 2]
        assert stats.robust_scatter(x) == pytest.approx(0.7413)

    def test_scatter_zeros(self):
        """Test a specific known case."""
        x = [0, 0, 0]
        assert stats.robust_scatter(x) == 0
