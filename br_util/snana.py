"""snana.py - utilities related to SNANA.
"""
import pandas as pd


def read_data(file_path, index_col=1, VERBOSE=False):
    with open(file_path, "r") as f:
        data = pd.read_csv(
            f, sep="\s+", comment="#", na_values=[-9, -99], index_col=index_col
        )
    data.drop(columns="VARNAMES:", inplace=True)
    if VERBOSE:
        print(data.describe())
    return data
