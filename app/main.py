"""
Segmentação de Clientes — Mall Customers
Entry point do app Streamlit.

Rodar localmente (a partir da raiz do projeto):
    streamlit run app/main.py
"""
import streamlit as st

from style import aplicar_estilo

st.set_page_config(
    page_title="Segmentação de Clientes — Mall",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded",
)

aplicar_estilo()

# ── Navegação (st.navigation requer streamlit >= 1.36) ───────────
paginas = [
    st.Page("pages/1_visao_geral.py", title="Visão Geral",        icon="📊"),
    st.Page("pages/2_clusters.py",    title="Personas & Clusters", icon="🎯"),
    st.Page("pages/3_classificar.py", title="Classificar Cliente", icon="🔮"),
]

with st.sidebar:
    st.markdown("## 🛍️ Mall Customers")
    st.caption("Segmentação de clientes · Pipeline sklearn + KMeans")
    st.divider()

nav = st.navigation(paginas)
nav.run()
