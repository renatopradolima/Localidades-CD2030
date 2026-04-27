# app.py
import streamlit as st
import pandas as pd
import os
import requests
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

# Carregar dados (cache) – DataFrame leve, sem geometria
with st.spinner("Carregando dados..."):
    df = carregar_dados()

# Barra lateral com navegação
aba = st.sidebar.radio(
    "Navegação",
    [
        "Diagnóstico Descritivo",
        "Distribuição Espacial",
    ]
)

# ================================================================
# Aba 1: Diagnóstico Descritivo
# ================================================================
if aba == "Diagnóstico Descritivo":
    st.header("Diagnóstico Descritivo")
    st.markdown(texto_intro())
    st.markdown(texto_nota_metodologica())

    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Registros", f"{len(df):,}")
    col2.metric("Categorias", df['CT_LOCALIDADE'].nunique())
    col3.metric("Unidades da Federação", df['SIGLA_UF'].nunique())

    st.subheader("Distribuição por Categoria")
    st.markdown(texto_pareto())

    freq, fig_pareto = criar_pareto(df)
    st.dataframe(
        freq.style.format({
            "Percentual": "{:.2f}%",
            "Percentual_Acumulado": "{:.2f}%"
        }),
        height=800
    )
    st.pyplot(fig_pareto, use_container_width=True)

    st.subheader("Distribuição Regional das Categorias")
    st.markdown(texto_contingencia())

    fig_barras = criar_barras_empilhadas(df)
    st.pyplot(fig_barras, use_container_width=True)

    pct_linha = pd.crosstab(
        df['CT_LOCALIDADE'], df['NM_GRANDE_REGIAO'], normalize='index'
    ) * 100
    st.dataframe(pct_linha.style.format("{:.1f}%"), height=600)

# ================================================================
# Aba 2: Distribuição Espacial
# ================================================================
elif aba == "Distribuição Espacial":
    st.header("Distribuição Espacial das Localidades")
    st.markdown("""
    Os mapas abaixo foram **pré‑renderizados integralmente** a partir do conjunto
    completo de localidades (sem amostragem). O processamento pesado foi realizado
    no Google Colab, e o dashboard apenas exibe os arquivos HTML estáticos,
    garantindo desempenho estável sem estouro de memória.
    """)

    # ----- Mapa de Cluster -----
    st.subheader("🗺️ Mapa de Pontos (todas as localidades)")

    @st.cache_resource
    def carregar_html_mapa():
        url = "https://github.com/renatopradolima/Localidades-CD2030/releases/download/mapas-v1/mapa_cluster.html"
        resp = requests.get(url)
        resp.raise_for_status()
        return resp.text

    with st.spinner("Carregando mapa de cluster… (pode levar alguns segundos)"):
        try:
            html_mapa = carregar_html_mapa()
            # Altura fixa 800 px
            st.components.v1.html(html_mapa, height=800, scrolling=True)
        except Exception as e:
            st.warning(f"⚠️ Mapa de cluster não disponível.\nErro: {e}")

    # Botão para abrir em tela cheia (nova aba)
    st.markdown("""
    <a href="https://github.com/renatopradolima/Localidades-CD2030/releases/download/mapas-v1/mapa_cluster.html" 
       target="_blank" style="text-decoration:none;">
       <button style="padding:8px 16px; font-size:14px; cursor:pointer;">🔲 Abrir mapa em tela cheia</button>
    </a>
    """, unsafe_allow_html=True)

    # ----- Mapas de Calor -----
    st.subheader("🔥 Mapas de Calor por Categoria")
    categorias_disponiveis = sorted([
        f.replace('.html', '').replace('_', ' ')
        for f in os.listdir("resultados/mapas")
        if f.endswith('.html') and f != 'mapa_cluster.html'
    ])

    if categorias_disponiveis:
        categoria_escolhida = st.selectbox(
            "Selecione a categoria para visualizar o mapa de calor:",
            categorias_disponiveis
        )
        nome_arquivo = categoria_escolhida.replace(' ', '_') + '.html'
        calor_path = os.path.join("resultados/mapas", nome_arquivo)

        if os.path.exists(calor_path):
            with open(calor_path, "r", encoding="utf-8") as f:
                st.components.v1.html(f.read(), height=800, scrolling=True)
            # Botão tela cheia
            st.markdown(f"""
            <a href="{calor_path}" target="_blank" style="text-decoration:none;">
               <button style="padding:8px 16px; font-size:14px; cursor:pointer;">🔲 Abrir mapa de calor em tela cheia</button>
            </a>
            """, unsafe_allow_html=True)
        else:
            st.warning(f"Mapa de calor para '{categoria_escolhida}' não encontrado.")
    else:
        st.warning("⚠️ Nenhum mapa de calor encontrado. Execute o notebook de geração no Colab.")

st.sidebar.markdown("---")
st.sidebar.info("Grupo de Trabalho Localidades • IBGE • Censo 2030")
