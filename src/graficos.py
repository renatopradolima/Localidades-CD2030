# src/graficos.py
import matplotlib.pyplot as plt
import pandas as pd

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

    # Adicionar rótulos de percentual nas barras
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
