# src/graficos.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def criar_pareto(gdf):
    """Gera a tabela de frequências e o gráfico de Pareto."""
    freq = gdf['CT_LOCALIDADE'].value_counts().reset_index()
    freq.columns = ['Categoria', 'Quantidade']
    freq['Percentual'] = (freq['Quantidade'] / len(gdf) * 100)
    freq = freq.sort_values('Quantidade', ascending=False)
    freq['Percentual_Acumulado'] = freq['Percentual'].cumsum()

    fig, ax1 = plt.subplots(figsize=(12, 6))
    ax1.bar(freq['Categoria'], freq['Quantidade'], color='steelblue')
    ax1.set_ylabel('Quantidade', fontsize=12)
    ax1.set_xlabel('Categoria')
    ax1.tick_params(axis='x', rotation=45)

    ax2 = ax1.twinx()
    ax2.plot(freq['Categoria'], freq['Percentual_Acumulado'], color='red', marker='o')
    ax2.set_ylabel('Percentual Acumulado (%)', color='red')

    for i, (qtd, pct) in enumerate(zip(freq['Quantidade'], freq['Percentual'])):
        ax1.text(i, qtd + 50, f"{pct:.1f}%", ha='center', fontsize=8)

    plt.tight_layout()
    return freq, fig


def criar_barras_empilhadas(gdf):
    """Gera o gráfico de barras empilhadas por categoria e região."""
    pct_linha = pd.crosstab(
        gdf['CT_LOCALIDADE'], gdf['NM_GRANDE_REGIAO'], normalize='index'
    ) * 100
    fig, ax = plt.subplots(figsize=(14, 7))
    pct_linha.plot(kind='bar', ax=ax, colormap='Set2')
    ax.set_title('Distribuição Percentual de Cada Categoria por Grande Região')
    ax.set_xlabel('Categoria')
    ax.set_ylabel('Percentual (%)')
    ax.legend(title='Região', bbox_to_anchor=(1.05, 1))
    plt.tight_layout()
    return fig


def criar_boxplot_porte(df_porte):
    """Boxplot de domicílios por categoria (escala log), removendo zeros."""
    # Filtrar apenas domicílios > 0 para a escala log
    df_plot = df_porte[df_porte['domicilios'] > 0].copy()
    if df_plot.empty:
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.text(0.5, 0.5, 'Nenhum valor positivo disponível para o boxplot.',
                ha='center', va='center', fontsize=12)
        ax.set_title('Boxplot – Domicílios por Categoria (escala log)')
        plt.tight_layout()
        return fig
    
    fig, ax = plt.subplots(figsize=(14, 7))
    sns.boxplot(data=df_plot, x='CT_LOCALIDADE', y='domicilios', ax=ax,
                order=sorted(df_plot['CT_LOCALIDADE'].unique()))
    ax.set_yscale('log')
    ax.set_title('Distribuição do Número de Domicílios por Categoria (escala log)')
    ax.set_xlabel('Categoria da Localidade')
    ax.set_ylabel('Domicílios (log)')
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    return fig


def criar_histogramas_porte(df_porte):
    """Histogramas de domicílios por categoria principal (exclui outliers)."""
    categorias = ['Povoado', 'Núcleo Urbano', 'Lugarejo', 'Outras Localidades',
                  'Localidade Indígena', 'Localidade Quilombola']
    df_filt = df_porte[df_porte['CT_LOCALIDADE'].isin(categorias)]
    if df_filt.empty:
        fig, ax = plt.subplots(figsize=(8, 4))
        ax.text(0.5, 0.5, 'Nenhum dado disponível para os histogramas.',
                ha='center', va='center', fontsize=12)
        plt.tight_layout()
        return fig
    
    q99 = df_filt['domicilios'].quantile(0.99)
    df_filt = df_filt[df_filt['domicilios'] < q99]
    g = sns.FacetGrid(df_filt, col='CT_LOCALIDADE', col_wrap=3,
                      sharex=False, sharey=False, height=4)
    g.map(sns.histplot, 'domicilios', bins=30, kde=True)
    g.fig.suptitle('Distribuição de Domicílios por Categoria (excluindo outliers)', y=1.02)
    plt.tight_layout()
    return g.fig
