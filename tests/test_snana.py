from pathlib import Path

from br_util import snana


class TestReadData:
    def test_read_data(self):
        # needs to be relative to where pytest is called, assume root of project
        mock_input_file = Path("tests/test_data") / Path("mock_INPUT_FITOPT000.FITRES")
        data = snana.read_data(mock_input_file)
        assert data.shape == (18, 52)
