"""
Identidade visual do app — GitHub Dark Theme.
Espelha a paleta de src/viz_config.py para manter coerência com as figuras.
"""
import streamlit as st

# ── Paleta GitHub Dark (idêntica a src/viz_config.CORES) ─────────
CORES = {
    "azul":     "#58a6ff",
    "verde":    "#3fb950",
    "roxo":     "#d2a8ff",
    "laranja":  "#ffa657",
    "vermelho": "#ff7b72",
    "amarelo":  "#e3b341",
    "texto":    "#e6edf3",
    "texto2":   "#8b949e",
    "fundo":    "#0d1117",
    "surf":     "#161b22",
    "borda":    "#30363d",
}

# Paleta de cores por cluster (idêntica a viz_config.PALETTE)
PALETTE = ["#58a6ff", "#ff7b72", "#3fb950", "#d2a8ff", "#ffa657",
           "#79c0ff", "#ffa198", "#56d364", "#e3b341", "#f78166"]


def aplicar_estilo():
    """Injeta CSS para reforçar o tema dark além do config.toml."""
    c = CORES
    st.markdown(f"""
    <style>
      .stApp {{ background:{c['fundo']}; }}
      h1, h2, h3 {{ color:{c['azul']}; }}
      .stMetric {{
        background:{c['surf']};
        border:1px solid {c['borda']};
        border-radius:8px;
        padding:14px;
      }}
      [data-testid="stMetricValue"] {{ color:{c['verde']}; }}
      [data-testid="stMetricLabel"] {{ color:{c['texto2']}; }}
      .persona-card {{
        background:{c['surf']};
        border:1px solid {c['borda']};
        border-left:4px solid {c['azul']};
        border-radius:8px;
        padding:16px 20px;
        margin:8px 0;
      }}
      .persona-card h4 {{ color:{c['azul']}; margin:0 0 6px 0; }}
      .persona-card p  {{ color:{c['texto2']}; margin:0; font-size:0.9em; }}
      .resultado-box {{
        background:{c['surf']};
        border:2px solid {c['verde']};
        border-radius:12px;
        padding:24px;
        text-align:center;
        margin:16px 0;
      }}
      .resultado-box .persona {{ color:{c['verde']}; font-size:1.8em; font-weight:bold; }}
      .resultado-box .desc    {{ color:{c['texto2']}; font-size:1em; margin-top:8px; }}
    </style>
    """, unsafe_allow_html=True)
