"""
Página 3 — Classificar um novo cliente (inferência ponta a ponta).
Demonstra o pipeline_final.predict() em uma única chamada.
"""
import streamlit as st
import plotly.express as px

from utils import (carregar_pipeline, carregar_features,
                   carregar_personas, classificar_cliente)
from style import CORES, PALETTE

st.title("🔮 Classificar Cliente")
st.caption("Informe os dados de um cliente e descubra a qual persona ele pertence.")

pipeline = carregar_pipeline()
features = carregar_features()
personas = carregar_personas()

# ── Formulário de entrada ────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    genero = st.selectbox("Gênero", ["Female", "Male"])
    idade  = st.slider("Idade", 18, 70, 30)
with col2:
    renda  = st.slider("Renda anual (k$)", 15, 140, 60)
    gasto  = st.slider("Score de gasto (1–100)", 1, 100, 50)

if st.button("Classificar", type="primary", use_container_width=True):
    cluster = classificar_cliente(pipeline, genero, idade, renda, gasto)
    info    = personas[str(cluster)]
    cor     = PALETTE[cluster % len(PALETTE)]

    # ── Resultado ────────────────────────────────────────────────
    st.markdown(f"""
    <div class="resultado-box" style="border-color:{cor}">
      <div class="persona" style="color:{cor}">{info['nome']}</div>
      <div class="desc">{info['descricao']}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Onde o cliente cai no mapa ───────────────────────────────
    st.markdown("### Posição do cliente no mapa")
    base = features.reset_index()
    fig = px.scatter(
        base, x="renda_anual", y="score_gasto",
        color="persona", color_discrete_sequence=PALETTE,
        opacity=0.45,
        labels={"renda_anual": "Renda anual (k$)", "score_gasto": "Score de gasto"},
    )
    # marca o cliente novo com uma estrela grande
    fig.add_scatter(
        x=[renda], y=[gasto], mode="markers",
        marker=dict(symbol="star", size=26, color="white",
                    line=dict(color="black", width=2)),
        name="Cliente novo",
    )
    fig.update_layout(
        plot_bgcolor=CORES["surf"], paper_bgcolor=CORES["fundo"],
        font_color=CORES["texto"], legend_title_text="", height=500,
    )
    fig.update_xaxes(gridcolor=CORES["borda"])
    fig.update_yaxes(gridcolor=CORES["borda"])
    st.plotly_chart(fig, use_container_width=True)

    st.info("ℹ️ A classificação usa `pipeline_final.predict()` — dados crus "
            "entram, persona sai, em uma única chamada. O gênero é descartado "
            "internamente pelo pipeline (não influencia o cluster).")
else:
    st.info("Ajuste os controles acima e clique em **Classificar**.")
