"""snana.py - utilities related to SNANA.
"""
import pandas as pd


def read_data(file_path, VERBOSE=False):
    with open(file_path, "r") as f:
        data = pd.read_csv(f, sep="\s+", comment="#", index_col=1)
    data.drop(columns="VARNAMES:", inplace=True)
    if VERBOSE:
        print(data.describe())
    return data
