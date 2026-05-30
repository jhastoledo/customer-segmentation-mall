"""
Carregamento centralizado dos artefatos de deploy + helpers.

Resolve caminhos via Path(__file__) para funcionar tanto localmente
quanto no Streamlit Cloud, independente do diretório de execução.
"""
from pathlib import Path
import json

import joblib
import pandas as pd
import streamlit as st

# ── Caminhos robustos (app/ -> raiz do projeto) ──────────────────
ROOT       = Path(__file__).resolve().parent.parent
MODELS_DIR = ROOT / "models"
DATA_DIR   = ROOT / "data" / "processed"

# ── Métricas de validação (documentadas no NB05) ─────────────────
METRICAS = {
    "silhouette":        0.428,
    "davies_bouldin":    0.825,
    "calinski_harabasz": 135.1,
    "fidelidade_surrogate": 0.925,
}

NUMERICAS = ["idade", "renda_anual", "score_gasto"]


@st.cache_resource
def carregar_pipeline():
    """Carrega o artefato único de deploy (preprocessor → KMeans)."""
    return joblib.load(MODELS_DIR / "pipeline_final.joblib")


@st.cache_data
def carregar_features() -> pd.DataFrame:
    """Carrega os clientes com cluster + persona (base do app)."""
    return pd.read_parquet(DATA_DIR / "features.parquet")


@st.cache_data
def carregar_personas() -> dict:
    """Carrega o dicionário cluster -> {nome, descrição}."""
    with open(MODELS_DIR / "personas.json", encoding="utf-8") as f:
        return json.load(f)


def cor_por_cluster(cluster: int, palette: list) -> str:
    """Cor consistente para um cluster (cicla na paleta se necessário)."""
    return palette[cluster % len(palette)]


def classificar_cliente(pipeline, genero, idade, renda, gasto):
    """
    Inferência ponta a ponta: dados crus -> cluster.
    O pipeline descarta 'genero' internamente, mas ele é passado
    para manter a assinatura RAW de 4 colunas que o pipeline espera.
    """
    cliente = pd.DataFrame([{
        "genero":      genero,
        "idade":       idade,
        "renda_anual": renda,
        "score_gasto": gasto,
    }])
    return int(pipeline.predict(cliente)[0])
