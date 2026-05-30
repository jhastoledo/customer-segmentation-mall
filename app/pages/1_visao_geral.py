"""
Página 1 — Visão Geral do projeto.
"""
import streamlit as st
import plotly.express as px

from utils import (carregar_features, carregar_personas, METRICAS)
from style import CORES, PALETTE

st.title("📊 Segmentação de Clientes — Mall Customers")
st.caption("Clustering não supervisionado · Pipeline sklearn + KMeans (k=6)")

features = carregar_features()
personas = carregar_personas()

# ── Métricas principais ──────────────────────────────────────────
st.markdown("### Resumo")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Clientes", len(features))
col2.metric("Personas", features["persona"].nunique())
col3.metric("Silhouette ↑", f"{METRICAS['silhouette']:.3f}")
col4.metric("Fidelidade surrogate", f"{METRICAS['fidelidade_surrogate']:.0%}")

st.divider()

# ── Cards das personas ───────────────────────────────────────────
st.markdown("### As 6 personas")
resumo = (features.groupby("persona")
          .agg(n=("cluster", "size"),
               idade=("idade", "mean"),
               renda=("renda_anual", "mean"),
               gasto=("score_gasto", "mean"))
          .round(1).sort_values("n", ascending=False))

# mapear nome da persona -> cluster (para a cor)
nome_para_cluster = {info["nome"]: int(c) for c, info in personas.items()}

colunas = st.columns(2)
for i, (nome, row) in enumerate(resumo.iterrows()):
    cluster = nome_para_cluster.get(nome, 0)
    cor = PALETTE[cluster % len(PALETTE)]
    desc = personas[str(cluster)]["descricao"]
    with colunas[i % 2]:
        st.markdown(f"""
        <div class="persona-card" style="border-left-color:{cor}">
          <h4 style="color:{cor}">{nome} · {int(row.n)} clientes</h4>
          <p>{desc}</p>
          <p>Idade {row.idade:.0f} · Renda {row.renda:.0f}k · Gasto {row.gasto:.0f}</p>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# ── Distribuição dos clientes (renda × gasto) ────────────────────
st.markdown("### Mapa dos clientes (Renda × Score de Gasto)")
fig = px.scatter(
    features.reset_index(),
    x="renda_anual", y="score_gasto",
    color="persona",
    color_discrete_sequence=PALETTE,
    hover_data=["idade", "genero"],
    labels={"renda_anual": "Renda anual (k$)", "score_gasto": "Score de gasto"},
)
fig.update_layout(
    plot_bgcolor=CORES["surf"], paper_bgcolor=CORES["fundo"],
    font_color=CORES["texto"], legend_title_text="Persona",
    height=520,
)
fig.update_xaxes(gridcolor=CORES["borda"])
fig.update_yaxes(gridcolor=CORES["borda"])
st.plotly_chart(fig, use_container_width=True)
