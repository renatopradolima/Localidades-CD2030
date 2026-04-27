# app.py
import streamlit as st
import pandas as pd
import os
from src.dados import carregar_dados
from src.graficos import criar_pareto, criar_barras_empilhadas
from src.interpretacoes import (
    texto_intro,
    texto_nota_metodologica,
    texto_pareto,
    texto_contingencia,
)

st.set_page_config(page_title="Localidades CD2030", layout="wide")
st.title("🔎 Localidades do Brasil – Censo 2022")
st.markdown("Dashboard de diagnóstico para o Grupo de Trabalho de Localidades")

# Carregar dados (cache)
with st.spinner("Carregando dados..."):
    gdf = carregar_dados()

# Barra lateral com navegação
aba = st.sidebar.radio(
    "Navegação",
    [
        "Diagnóstico Descritivo",
        "Distribuição Espacial",
        # "Porte das Localidades",        # próxima aba
        # "Análise Multivariada (ACM)",   # próxima aba
        # "Disponibilidade de Serviços",  # próxima aba
    ]
)

# =====================================================================
# Aba 1: Diagnóstico Descritivo
# =====================================================================
if aba == "Diagnóstico Descritivo":
    st.header("Diagnóstico Descritivo")
    st.markdown(texto_intro())
    st.markdown(texto_nota_metodologica())

    # Métricas gerais
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Registros", f"{len(gdf):,}")
    col2.metric("Categorias", gdf['CT_LOCALIDADE'].nunique())
    col3.metric("Unidades da Federação", gdf['SIGLA_UF'].nunique())

    # Frequência e Pareto
    st.subheader("Distribuição por Categoria")
    st.markdown(texto_pareto())

    freq, fig_pareto = criar_pareto(gdf)
    st.dataframe(
        freq.style.format({
            "Percentual": "{:.2f}%",
            "Percentual_Acumulado": "{:.2f}%"
        }),
        height=800
    )
    st.pyplot(fig_pareto, use_container_width=True)

    # Contingência Categoria × Grande Região
    st.subheader("Distribuição Regional das Categorias")
    st.markdown(texto_contingencia())

    fig_barras = criar_barras_empilhadas(gdf)
    st.pyplot(fig_barras, use_container_width=True)

    pct_linha = pd.crosstab(
        gdf['CT_LOCALIDADE'], gdf['NM_GRANDE_REGIAO'], normalize='index'
    ) * 100
    st.dataframe(pct_linha.style.format("{:.1f}%"), height=600)

# =====================================================================
# Aba 2: Distribuição Espacial (a ser preenchida com os mapas HTML)
# =====================================================================

elif aba == "Distribuição Espacial":
    st.header("Distribuição Espacial das Localidades")
    st.markdown("""
    Os mapas interativos abaixo mostram a localização de **todas** as localidades
    (sem amostragem) e a densidade por categoria.
    """)

    # ---- Mapa de pontos com cluster ----
    st.subheader("Mapa de Pontos (Cluster)")
    with st.spinner("Gerando mapa de pontos..."):
        from src.mapas import criar_mapa_cluster
        mapa_cluster = criar_mapa_cluster(gdf)
        from streamlit_folium import st_folium
        st_folium(mapa_cluster, width=1200, height=600)

    # ---- Mapas de calor por categoria ----
    st.subheader("Mapa de Calor por Categoria")
    categorias = list(gdf['CT_LOCALIDADE'].unique())
    categoria_escolhida = st.selectbox("Selecione a categoria:", categorias)

    from src.mapas import criar_mapa_calor_por_categoria
    with st.spinner(f"Gerando mapa de calor para '{categoria_escolhida}'..."):
        mapa_calor = criar_mapa_calor_por_categoria(gdf, categoria_escolhida)
        st_folium(mapa_calor, width=1200, height=600)

# =====================================================================
# Rodapé lateral
# =====================================================================
st.sidebar.markdown("---")
st.sidebar.info("Grupo de Trabalho Localidades • IBGE • Censo 2030")
