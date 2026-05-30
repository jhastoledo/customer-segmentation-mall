"""
Funções para carregamento, limpeza e divisão dos dados.

Exemplos do que pode conter:
    - carregar o dataset bruto
    - tratar valores ausentes
    - remover duplicatas
    - dividir em treino/validação/teste
    - salvar dados processados
"""

"""
Funções para carregamento, limpeza e divisão dos dados.
"""

import pandas as pd

# ── Mapeamento explícito: Mall Customers → snake_case PT-BR ──────
# Dict explícito (não regex) porque "Annual Income (k$)" tem
# parênteses/$/espaços que um regex ingênuo destruiria.
_RENOMEAR_COLUNAS = {
    "CustomerID":             "id_cliente",
    "Gender":                 "genero",
    "Genre":                  "genero",      # algumas versões do Kaggle usam "Genre"
    "Age":                    "idade",
    "Annual Income (k$)":     "renda_anual",
    "Spending Score (1-100)": "score_gasto",
}


def padronizar_colunas(df: pd.DataFrame) -> pd.DataFrame:
    """
    Renomeia as colunas do Mall Customers para snake_case em português.

    Fonte única de verdade para os nomes de coluna — usada no NB01 (EDA)
    e no NB02 (limpeza) para evitar divergência ao longo do pipeline.

    Parâmetros
    ----------
    df : pd.DataFrame
        DataFrame bruto recém-carregado do CSV.

    Retorna
    -------
    pd.DataFrame
        Mesmo DataFrame com colunas renomeadas.
    """
    df = df.rename(columns=_RENOMEAR_COLUNAS)

    nao_mapeadas = [c for c in df.columns if c not in _RENOMEAR_COLUNAS.values()]
    if nao_mapeadas:
        print(f"⚠️  Colunas sem mapeamento (mantidas como estão): {nao_mapeadas}")

    return df