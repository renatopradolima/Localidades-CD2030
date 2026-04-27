# src/mapas.py
import folium
from folium.plugins import MarkerCluster, HeatMap
import streamlit as st

def criar_mapa_cluster(gdf, centro=[-15, -55], zoom=4):
    """Mapa de pontos com agrupamento automático (MarkerCluster)."""
    mapa = folium.Map(location=centro, zoom_start=zoom, tiles='cartodb positron')

    # Criar uma lista de coordenadas e popups
    dados = []
    for _, row in gdf.iterrows():
        popup = folium.Popup(f"{row['CT_LOCALIDADE']}: {row['NM_LOCALIDADE']}", max_width=250)
        dados.append([row.geometry.y, row.geometry.x, popup])

    # Adicionar cluster
    marker_cluster = MarkerCluster(name="Localidades").add_to(mapa)
    for lat, lon, popup in dados:
        folium.Marker(location=[lat, lon], popup=popup).add_to(marker_cluster)

    folium.LayerControl().add_to(mapa)
    return mapa


def criar_mapa_calor_por_categoria(gdf, categoria, centro=[-15, -55], zoom=5):
    """Mapa de calor para uma categoria específica."""
    subset = gdf[gdf['CT_LOCALIDADE'] == categoria]
    mapa = folium.Map(location=centro, zoom_start=zoom, tiles='cartodb positron')

    # Extrair coordenadas
    coords = [[p.y, p.x] for p in subset.geometry]
    if coords:
        HeatMap(coords, radius=12, blur=15, max_zoom=1).add_to(mapa)

    folium.LayerControl().add_to(mapa)
    return mapa
