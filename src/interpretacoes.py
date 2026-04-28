# src/interpretacoes.py

def texto_intro():
    return """
    A base de **Localidades do Brasil** do Censo Demográfico 2022 reúne **96.163 registros**
    de aglomerados humanos, distribuídos em 12 categorias. Este número inclui as
    localidades com dupla classificação (ex.: uma comunidade quilombola que também é um
    lugarejo), que são contadas separadamente em cada categoria, totalizando um valor
    superior aos 87.362 pontos únicos disponíveis nos arquivos vetoriais.

    Nesta primeira etapa da análise, apresentamos as frequências absolutas e relativas de cada
    categoria e a sua distribuição pelas cinco Grandes Regiões do país. O objetivo é oferecer ao
    Grupo de Trabalho um panorama quantitativo inicial que evidencie a diversidade e a
    concentração das localidades, apoiando a definição de critérios metodológicos para o Censo 2030.
    """


def texto_nota_metodologica():
    return """
    ### Nota metodológica: registros vs. pontos únicos

    O total de **96.163 registros** exibido neste dashboard corresponde à soma das contagens
    por categoria. Esse valor supera os **87.362 pontos únicos** dos arquivos vetoriais
    publicados porque **8.775 localidades** receberam dupla classificação. Por exemplo, uma
    comunidade quilombola que também se enquadra como lugarejo é contabilizada duas vezes
    — uma em cada categoria — embora possua um único geocódigo e ponto no mapa.

    Essa dupla contagem não é um erro, mas sim uma consequência da metodologia adotada
    em 2022, que permitiu que uma localidade acumulasse mais de uma categoria para melhor
    representar suas múltiplas dimensões (ex.: identidade étnica + tipologia rural). O Grupo de
    Trabalho deve considerar se essa prática será mantida no Censo 2030 ou se será adotada
    uma classificação hierárquica que evite duplicidades.
    """


def texto_pareto():
    return """
    ### Como as localidades estão distribuídas por categoria?

    O gráfico de Pareto revela uma forte concentração: as três primeiras categorias —
    **Outras Localidades** (38.782; 40,3%), **Povoado** (16.500; 17,2%) e **Localidade Indígena**
    (9.185; 9,6%) — já acumulam mais de dois terços (67,0%) de todos os registros. Somando
    **Localidade Quilombola** (8.202; 8,5%), o patamar chega a 75,6%.

    A categoria **Outras Localidades** merece atenção especial: ela abrange os aglomerados
    com 10 a 49 domicílios que não puderam ser setorizados. Seu enorme volume reflete tanto o
    esforço inédito de mapeamento do Censo 2022 quanto a pulverização do povoamento em
    pequenas aglomerações, sobretudo no Nordeste (66,2% do total dessa categoria) e no
    Sudeste (22,7%).

    Na outra ponta, **Núcleo Rural** (242; 0,25%), **Regiões Administrativas do Distrito Federal**
    (33) e **Distrito Estadual de Fernando de Noronha** (1) são categorias residuais do ponto de
    vista numérico, mas com significado administrativo ou metodológico específico.
    """


def texto_contingencia():
    return """
    ### Onde estão as diferentes categorias?

    A tabela cruzada entre categoria e Grande Região evidencia associações espaciais nítidas,
    que refletem processos históricos, ambientais e institucionais de ocupação do território:

    - **Localidades Indígenas (Norte: 62,1%)**: das 9.185 localidades indígenas, 5.707 estão
      na Região Norte, principalmente no Amazonas e em Roraima.
    - **Localidades Quilombolas (Nordeste: 64,2%)**: a concentração no Nordeste (5.265 de
      8.202) está ligada ao legado histórico das comunidades remanescentes de quilombos.
    - **Povoados (Nordeste: 68,3%)** e **Lugarejos (Nordeste: 59,5%)**: essas categorias
      rurais, que somam juntas 21.273 registros, têm no Nordeste sua maior expressão,
      indicando uma estrutura de povoamento rural densa e dispersa.
    - **Núcleos Urbanos (Sudeste: 62,1%)**: reflexo de processos de urbanização difusa e da
      criação de loteamentos e condomínios, especialmente em São Paulo e Minas Gerais.
    - **Vilas (Sudeste: 34,5%)** e **Cidades (Sudeste: 29,9%)**: embora as cidades estejam
      distribuídas de forma mais equilibrada, a Região Sudeste lidera também nessas categorias
      urbanas, seguida pelo Sul.
    - **Outras Localidades (Nordeste: 66,2%)**: a pulverização de pequenos aglomerados é
      especialmente intensa no Maranhão, Bahia e Piauí.
    - **Agrovilas do PA (Nordeste: 79,5%)**: a forte presença no Nordeste está associada aos
      projetos de reforma agrária.
    - **Centro‑Oeste (4,0% do total)**: embora tenha a menor quantidade absoluta, destaca-se
      pelo crescimento relativo de Núcleos Urbanos e pela presença de todas as 33 Regiões
      Administrativas do Distrito Federal.

    Em síntese, o Nordeste concentra 54,9% de todos os registros (52.766), impulsionado
    principalmente pelas categorias rurais e pelas "Outras Localidades". O Norte abriga
    14,0% do total, mas com enorme peso das Localidades Indígenas. O Sudeste (20,1%) lidera
    nas categorias urbanas. Sul e Centro‑Oeste, juntos, respondem por 11,1% dos registros.
    """
