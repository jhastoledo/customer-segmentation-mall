"""Testes para src/data.py"""
import pandas as pd
import numpy as np
import pytest
from src.data import clean_data, split_data


def test_clean_data_remove_duplicatas():
    df = pd.DataFrame({"a": [1, 1, 2], "b": ["x", "x", "y"], "target": [0, 0, 1]})
    resultado = clean_data(df)
    assert len(resultado) == 2


def test_clean_data_imputa_nulos_numericos():
    df = pd.DataFrame({"a": [1.0, None, 3.0], "target": [0, 1, 0]})
    resultado = clean_data(df, imputar_numericas="mediana")
    assert resultado["a"].isna().sum() == 0


def test_split_data_shapes():
    df = pd.DataFrame({
        "f1": range(100), "f2": range(100),
        "Attrition": [0] * 80 + [1] * 20,
    })
    X_tr, X_v, X_te, y_tr, y_v, y_te = split_data(df)
    assert len(X_tr) + len(X_v) + len(X_te) == 100
