"""Testes para src/models.py"""
import pandas as pd
import numpy as np
from src.models import train_model


def test_train_baseline():
    X = pd.DataFrame({"f1": np.random.randn(50), "f2": np.random.randn(50)})
    y = pd.Series([0] * 25 + [1] * 25)
    modelo = train_model(X, y, tipo="baseline", validar_cv=False)
    preds = modelo.predict(X)
    assert len(preds) == 50


def test_train_logistic():
    X = pd.DataFrame({"f1": np.random.randn(60), "f2": np.random.randn(60)})
    y = pd.Series([0] * 30 + [1] * 30)
    modelo = train_model(X, y, tipo="logistic_regression",
                         params={"class_weight": "balanced", "random_state": 42},
                         validar_cv=False)
    assert hasattr(modelo, "predict_proba")
