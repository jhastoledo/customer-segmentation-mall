"""Testes para src/features.py"""
import pandas as pd
import numpy as np
from src.features import encode_categoricals, scale_numerics


def _make_splits():
    df = pd.DataFrame({
        "num": [1.0, 2.0, 3.0, 4.0, 5.0],
        "cat": ["a", "b", "a", "b", "c"],
    })
    return df[:3].copy(), df[3:4].copy(), df[4:].copy()


def test_encode_categoricals_no_unseen_error():
    tr, vl, te = _make_splits()
    tr2, vl2, te2 = encode_categoricals(tr, vl, te, colunas=["cat"])
    assert tr2["cat"].dtype != object


def test_scale_numerics_standard():
    tr, vl, te = _make_splits()
    tr2, _, _ = scale_numerics(tr, vl, te, colunas=["num"], metodo="standard")
    assert abs(tr2["num"].mean()) < 1e-9
