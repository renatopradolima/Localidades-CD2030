# src/dados.py
import streamlit as st
import geopandas as gpd
import pandas as pd
import gdown
import os

# ID do arquivo no Google Drive (compartilhado publicamente)
FILE_ID = "133yRXnCrimQgvA1xzQYSfxLIIVJFi5YO"

# Mapeamento UF -> Grande Região (caso necessário)
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
    
    # Baixa apenas se o arquivo não existir localmente
    if not os.path.exists(parquet_path):
        with st.spinner("Baixando dados processados do Google Drive..."):
            gdown.download(url, parquet_path, quiet=False)
    
    gdf = gpd.read_parquet(parquet_path)
    
    # Cria coluna de Grande Região se não existir
    if 'NM_GRANDE_REGIAO' not in gdf.columns:
        gdf['NM_GRANDE_REGIAO'] = gdf['SIGLA_UF'].map(SIGLA_PARA_REGIAO)
    
    return gdf
