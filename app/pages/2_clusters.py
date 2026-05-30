"""
Página 2 — Exploração detalhada de cada persona/cluster.
"""
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from utils import carregar_features, carregar_personas
from style import CORES, PALETTE

st.title("🎯 Personas & Clusters")

features = carregar_features()
personas = carregar_personas()

# ── Seletor de persona ───────────────────────────────────────────
nomes = [personas[str(c)]["nome"] for c in sorted(personas, key=int)]
escolha = st.selectbox("Selecione uma persona para detalhar:", nomes)

cluster_sel = next(int(c) for c, info in personas.items()
                   if info["nome"] == escolha)
cor = PALETTE[cluster_sel % len(PALETTE)]
sub = features[features["cluster"] == cluster_sel]

# ── Perfil da persona selecionada ────────────────────────────────
st.markdown(f"<h3 style='color:{cor}'>{escolha}</h3>", unsafe_allow_html=True)
st.caption(personas[str(cluster_sel)]["descricao"])

c1, c2, c3, c4 = st.columns(4)
c1.metric("Clientes", len(sub))
c2.metric("Idade média", f"{sub['idade'].mean():.0f}")
c3.metric("Renda média", f"{sub['renda_anual'].mean():.0f}k")
c4.metric("Gasto médio", f"{sub['score_gasto'].mean():.0f}")

# composição de gênero
genero_pct = sub["genero"].value_counts(normalize=True).mul(100).round(0)
st.caption("Composição de gênero: " +
           " · ".join(f"{g} {p:.0f}%" for g, p in genero_pct.items()))

st.divider()

# ── Scatter destacando a persona selecionada ─────────────────────
st.markdown("### Posição no mapa de clientes")
features_plot = features.reset_index().copy()
features_plot["destaque"] = features_plot["cluster"].apply(
    lambda x: escolha if x == cluster_sel else "Outras personas")

fig = px.scatter(
    features_plot, x="renda_anual", y="score_gasto",
    color="destaque",
    color_discrete_map={escolha: cor, "Outras personas": CORES["texto2"]},
    hover_data=["idade", "persona"],
    labels={"renda_anual": "Renda anual (k$)", "score_gasto": "Score de gasto"},
)
fig.update_traces(marker=dict(size=9, opacity=0.85),
                  selector=dict(name=escolha))
fig.update_traces(marker=dict(size=6, opacity=0.25),
                  selector=dict(name="Outras personas"))
fig.update_layout(
    plot_bgcolor=CORES["surf"], paper_bgcolor=CORES["fundo"],
    font_color=CORES["texto"], legend_title_text="", height=480,
)
fig.update_xaxes(gridcolor=CORES["borda"])
fig.update_yaxes(gridcolor=CORES["borda"])
st.plotly_chart(fig, use_container_width=True)

st.divider()

# ── Comparativo: perfil médio de todas as personas (radar) ───────
st.markdown("### Comparativo entre personas")
perfil = features.groupby("cluster")[["idade", "renda_anual", "score_gasto"]].mean()
# normalização min-max para o radar
perfil_norm = (perfil - features[["idade", "renda_anual", "score_gasto"]].min()) / \
              (features[["idade", "renda_anual", "score_gasto"]].max() -
               features[["idade", "renda_anual", "score_gasto"]].min())

radar = go.Figure()
eixos = ["idade", "renda_anual", "score_gasto"]
for c in sorted(perfil_norm.index):
    nome = personas[str(c)]["nome"]
    valores = perfil_norm.loc[c, eixos].tolist()
    radar.add_trace(go.Scatterpolar(
        r=valores + [valores[0]],
        theta=eixos + [eixos[0]],
        name=nome,
        line_color=PALETTE[c % len(PALETTE)],
    ))
radar.update_layout(
    polar=dict(bgcolor=CORES["surf"],
               radialaxis=dict(visible=True, range=[0, 1], gridcolor=CORES["borda"])),
    paper_bgcolor=CORES["fundo"], font_color=CORES["texto"], height=520,
)
st.plotly_chart(radar, use_container_width=True)
