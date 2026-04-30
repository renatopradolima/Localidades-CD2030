# src/dados.py
import streamlit as st
import pandas as pd
import gdown
import os

FILE_ID = "133yRXnCrimQgvA1xzQYSfxLIIVJFi5YO"

SIGLA_PARA_REGIAO = {
    'RO': 'Norte', 'AC': 'Norte', 'AM': 'Norte', 'RR': 'Norte', 'PA': 'Norte',
    'AP': 'Norte', 'TO': 'Norte',
    'MA': 'Nordeste', 'PI': 'Nordeste', 'CE': 'Nordeste', 'RN': 'Nordeste',
    'PB': 'Nordeste', 'PE': 'Nordeste', 'AL': 'Nordeste', 'SE': 'Nordeste',
    'BA': 'Nordeste',
    'MG': 'Sudeste', 'ES': 'Sudeste', 'RJ': 'Sudeste', 'SP': 'Sudeste',
    'PR': 'Sul', 'SC': 'Sul', 'RS': 'Sul',
    'MS': 'Centro-Oeste', 'MT': 'Centro-Oeste', 'GO': 'Centro-Oeste',
    'DF': 'Centro-Oeste'
}

@st.cache_data
def carregar_dados():
    url = f"https://drive.google.com/uc?id={FILE_ID}"
    parquet_path = "localidades_2022_processado.parquet"
    
    if not os.path.exists(parquet_path):
        with st.spinner("Baixando dados processados do Google Drive..."):
            gdown.download(url, parquet_path, quiet=False)
    
    # Carregar APENAS as colunas necessárias, SEM geometria
    colunas = ['CT_LOCALIDADE', 'SIGLA_UF', 'NM_GRANDE_REGIAO']
    df = pd.read_parquet(parquet_path, columns=colunas)
    
    # Criar coluna de Grande Região se não existir
    if 'NM_GRANDE_REGIAO' not in df.columns:
        df['NM_GRANDE_REGIAO'] = df['SIGLA_UF'].map(SIGLA_PARA_REGIAO)
    
    return df

# (conteúdo existente de src/dados.py permanece...)

FILE_ID_PORTE = "1cO96z09CbNBzPl2FVlerS03rPt89s4Qz"

@st.cache_data
def carregar_porte():
    """Baixa e carrega o dataset de porte das localidades."""
    url = f"https://drive.google.com/uc?id={FILE_ID_PORTE}"
    path = "porte_localidades.parquet"
    if not os.path.exists(path):
        with st.spinner("Baixando dados de porte..."):
            gdown.download(url, path, quiet=False)
    return pd.read_parquet(path)
