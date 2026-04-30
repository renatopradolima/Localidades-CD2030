import streamlit as st
import pandas as pd
import geopandas as gpd
import gdown
import os

# ID do arquivo de localidades processadas
FILE_ID = "133yRXnCrimQgvA1xzQYSfxLIIVJFi5YO"

# ID do arquivo de porte (substitua pelo novo)
FILE_ID_PORTE = "1cO96z09CbNBzPl2FVlerS03rPt89s4Qz"

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
    
    colunas = ['CT_LOCALIDADE', 'SIGLA_UF', 'NM_GRANDE_REGIAO']
    df = pd.read_parquet(parquet_path, columns=colunas)
    
    if 'NM_GRANDE_REGIAO' not in df.columns:
        df['NM_GRANDE_REGIAO'] = df['SIGLA_UF'].map(SIGLA_PARA_REGIAO)
    
    return df


@st.cache_data
def carregar_porte():
    url = f"https://drive.google.com/uc?id={FILE_ID_PORTE}"
    parquet_path = "porte_localidades.parquet"
    
    if not os.path.exists(parquet_path):
        with st.spinner("Baixando dados de porte..."):
            gdown.download(url, parquet_path, quiet=False)
    
    return pd.read_parquet(parquet_path)
