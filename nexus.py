import pandas as pd
from typing import List, Dict, Any, Tuple, Set

# Dados de entrada

def get_dados_cursos() -> List[Dict[str, Any]]:

    #Retorna a lista de dicionários contendo os dados dos cursos.
    #Cada curso tem: Nome, Tempo_Horas (peso) e Impacto_Valor (valor).

    return [
        {"Nome": "Python para Data Science", "Tempo_Horas": 8, "Impacto_Valor": 75},
        {"Nome": "Machine Learning (Básico)", "Tempo_Horas": 12, "Impacto_Valor": 90},
        {"Nome": "Fundamentos de Cloud (AWS)", "Tempo_Horas": 6, "Impacto_Valor": 60},
        {"Nome": "Comunicação Efetiva", "Tempo_Horas": 4, "Impacto_Valor": 50},
        {"Nome": "Metodologias Ágeis (Scrum)", "Tempo_Horas": 5, "Impacto_Valor": 55},
        {"Nome": "SQL para Análise de Dados", "Tempo_Horas": 7, "Impacto_Valor": 70},
        {"Nome": "Deep Learning (Intro)", "Tempo_Horas": 10, "Impacto_Valor": 85},
        {"Nome": "Gestão de Projetos (PMP)", "Tempo_Horas": 15, "Impacto_Valor": 95},
        {"Nome": "Power BI (Dashboards)", "Tempo_Horas": 6, "Impacto_Valor": 65},
        {"Nome": "Finanças para Não-Financeiros", "Tempo_Horas": 5, "Impacto_Valor": 45},
        {"Nome": "Introdução a Cibersegurança", "Tempo_Horas": 4, "Impacto_Valor": 60},
        {"Nome": "Design Thinking", "Tempo_Horas": 3, "Impacto_Valor": 40},
        {"Nome": "IA Generativa (Fundamentos)", "Tempo_Horas": 5, "Impacto_Valor": 80},
        {"Nome": "Inglês para Negócios", "Tempo_Horas": 10, "Impacto_Valor": 70},
        {"Nome": "Marketing Digital (SEO)", "Tempo_Horas": 6, "Impacto_Valor": 50},
        {"Nome": "Excel Avançado", "Tempo_Horas": 7, "Impacto_Valor": 60},
        {"Nome": "Liderança e Gestão de Pessoas", "Tempo_Horas": 8, "Impacto_Valor": 75},
        {"Nome": "Programação em R", "Tempo_Horas": 9, "Impacto_Valor": 70},
        {"Nome": "Automação (RPA)", "Tempo_Horas": 5, "Impacto_Valor": 65},
        {"Nome": "Big Data (Conceitos)", "Tempo_Horas": 4, "Impacto_Valor": 55},
        {"Nome": "Desenvolvimento Pessoal", "Tempo_Horas": 3, "Impacto_Valor": 30},
        {"Nome": "Blockchain (Básico)", "Tempo_Horas": 2, "Impacto_Valor": 25},
    ]

# Estrutura de dados

def criar_dataframe_cursos() -> pd.DataFrame:
    #Cria e retorna um DataFrame do Pandas com os dados dos cursos.
    
    dados = get_dados_cursos()
    df = pd.DataFrame(dados)
    # Adiciona um ID único para facilitar o rastreamento
    df['ID'] = range(len(df))
    df = df[['ID', 'Nome', 'Tempo_Horas', 'Impacto_Valor']]
    return df

# Função de ordenação recursiva (Merge Sort)

def merge(left: List[Dict], right: List[Dict], key: str) -> List[Dict]:
    
    #Função auxiliar do Merge Sort.
    #Mescla duas listas de dicionários ordenadas com base em uma 'key'.
    
    resultado = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i][key] <= right[j][key]:
            resultado.append(left[i])
            i += 1
        else:
            resultado.append(right[j])
            j += 1
    # Adiciona os elementos restantes
    resultado.extend(left[i:])
    resultado.extend(right[j:])
    return resultado

def merge_sort(items: List[Dict], key: str = 'Impacto_Valor') -> List[Dict]:
    """
    Implementação recursiva do Merge Sort (Top-Down).
    Ordena uma lista de dicionários (cursos) com base em uma chave (key).

    Parâmetros:
    - items (list): A lista de dicionários (cursos) a ser ordenada.
    - key (str): A chave do dicionário (ex: 'Impacto_Valor') pela qual ordenar.

    Retorna:
    - list: Uma nova lista contendo os itens ordenados.
    """
    # Caso base
    if len(items) <= 1:
        return items

    # Passo recursivo:
    mid = len(items) // 2
    left_half = items[:mid]
    right_half = items[mid:]
    sorted_left = merge_sort(left_half, key)
    sorted_right = merge_sort(right_half, key)
    return merge(sorted_left, sorted_right, key)

# SOLUÇÃO DA MOCHILA

def knapsack_recursivo(
    memo: Dict[Tuple[int, int], Tuple[float, Set[int]]],
    tempos: List[int],
    impactos: List[float],
    ids_cursos: List[int],
    capacidade: int,
    n: int
) -> Tuple[float, Set[int]]:
    """
    Função recursiva principal para o Problema da Mochila.

    Parâmetros:
    - memo (dict): Dicionário de memoização para armazenar resultados (Impacto, {IDs})
    - tempos (list): Lista de pesos (Tempo_Horas) dos cursos.
    - impactos (list): Lista de valores (Impacto_Valor) dos cursos.
    - ids_cursos (list): Lista dos IDs originais dos cursos.
    - capacidade (int): A capacidade restante da mochila (horas restantes).
    - n (int): O número de itens (cursos) que estamos considerando (do índice 0 até n-1).

    Retorna:
    - Tuple[float, Set[int]]: Uma tupla contendo:
        O valor máximo de impacto alcançável.
        Um conjunto (set) com os IDs dos cursos selecionados.
    """
    
    # Chave para memoização: (itens restantes, capacidade restante)
    chave_memo = (n, capacidade)

    # Consulta
    # Se já calculamos para este estado (n, capacidade), retorna o resultado salvo.
    if chave_memo in memo:
        return memo[chave_memo]

    # CASOS BASE DA RECURSÃO
    # Se não há mais itens (n=0) ou não há mais capacidade (capacidade=0),
    # o impacto é 0 e nenhum curso é selecionado.
    if n == 0 or capacidade == 0:
        return (0.0, set())

    # Índice do item atual (estamos processando do item n-1 para 0)
    # Ex: n=5, estamos olhando o item de índice 4
    idx_atual = n - 1
    tempo_item_atual = tempos[idx_atual]
    impacto_item_atual = impactos[idx_atual]
    id_item_atual = ids_cursos[idx_atual]

    # PASSO RECURSIVO
    # Caso A: O curso atual (n-1) não cabe na capacidade restante.
    # Temos que pular este curso.
    if tempo_item_atual > capacidade:
        # A solução é a mesma que resolver o problema para (n-1) itens.
        resultado = knapsack_recursivo(memo, tempos, impactos, ids_cursos, capacidade, n - 1)
    
    # Caso B: O curso atual CABE.
    # Temos que decidir qual é o melhor: (1) Incluir o curso ou (2) Excluir o curso.
    else:
        # Decisão 1: EXCLUIR o curso atual
        # Resolvemos o problema para (n-1) itens com a mesma capacidade.
        impacto_sem_item, cursos_sem_item = knapsack_recursivo(
            memo, tempos, impactos, ids_cursos, capacidade, n - 1
        )

        # Decisão 2: INCLUIR o curso atual
        # Resolvemos o problema para (n-1) itens com a capacidade REDUZIDA.
        # Somamos o impacto deste item ao resultado da sub-chamada.
        impacto_com_item_sub, cursos_com_item_sub = knapsack_recursivo(
            memo, tempos, impactos, ids_cursos, capacidade - tempo_item_atual, n - 1
        )
        
        impacto_com_item = impacto_item_atual + impacto_com_item_sub
        
        # Compara os impactos totais
        if impacto_com_item > impacto_sem_item:
            # Incluir é melhor:
            cursos_selecionados = cursos_com_item_sub.copy()
            cursos_selecionados.add(id_item_atual)
            resultado = (impacto_com_item, cursos_selecionados)
        else:
            # Excluir é melhor:
            resultado = (impacto_sem_item, cursos_sem_item)

    # SALVAR NA MEMOIZAÇÃO
    # Salva o resultado encontrado para o estado (n, capacidade)
    memo[chave_memo] = resultado
    
    return resultado

def otimizar_trilha_nexus(df_cursos: pd.DataFrame, capacidade_total: int) -> pd.DataFrame:
    """
    Função principal que orquestra a otimização da trilha de aprendizagem.

    Parâmetros:
    - df_cursos (pd.DataFrame): O DataFrame contendo todos os cursos disponíveis.
    - capacidade_total (int): O tempo total (em horas) disponível para o profissional.

    Retorna:
    - pd.DataFrame: Um DataFrame contendo apenas os cursos da trilha otimizada.
    """
    # Prepara os dados do DataFrame para as listas que a função recursiva espera
    tempos = df_cursos['Tempo_Horas'].tolist()
    impactos = df_cursos['Impacto_Valor'].tolist()
    ids_cursos = df_cursos['ID'].tolist()
    n = len(df_cursos)

    # Dicionário de memoização (vazio no início)
    memo = {}

    # Chama a função recursiva principal
    impacto_maximo, ids_selecionados = knapsack_recursivo(
        memo, tempos, impactos, ids_cursos, capacidade_total, n
    )

    # Filtra o DataFrame original para retornar apenas os cursos selecionados
    df_selecionados = df_cursos[df_cursos['ID'].isin(ids_selecionados)].copy()
    
    # Ordena o resultado final para melhor visualização
    df_selecionados = df_selecionados.sort_values(by='Impacto_Valor', ascending=False)
    
    return df_selecionados

# EXECUÇÃO PRINCIPAL E RELATÓRIO DE SAÍDA

if __name__ == "__main__":
    
    # ---PARÂMETROS DE ENTRADA---
    CAPACIDADE_HORAS_PROFISSIONAL = 27 # (Altere aqui se desejar)
    
    # Carregar Dados
    df_cursos_disponiveis = criar_dataframe_cursos()
    print("---Plataforma NEXUS: Cursos Disponíveis---")
    print(f"Total de cursos na base: {len(df_cursos_disponiveis)}")
    print(f"Tempo total disponível do profissional: {CAPACIDADE_HORAS_PROFISSIONAL} horas\n")
    # print(df_cursos_disponiveis.to_string()) # Descomente para ver todos os cursos
    
    # Demonstração da Ordenação Recursiva (Merge Sort)
    # Nota: A ordenação não é necessária para a solução da mochila,
    # mas é um requisito do trabalho.
    print("--- (Demo) Ordenação Recursiva (Merge Sort) ---")
    # Convertemos o DF para lista de dicts para usar a função recursiva
    lista_de_cursos = df_cursos_disponiveis.to_dict('records')
    # Ordenando por 'Impacto_Valor' de forma decrescente (modificando o merge)
    # ou simplesmente ordenando e invertendo:
    cursos_ordenados = merge_sort(lista_de_cursos, key='Impacto_Valor')
    df_ordenado = pd.DataFrame(cursos_ordenados)
    print("Cursos ordenados por Impacto (Top 5):")
    print(df_ordenado.sort_values(by='Impacto_Valor', ascending=False).head(5))
    print("-" * 40 + "\n")

    # Executar a Otimização (Programação Dinâmica)
    print("Executando o otimizador de trilha (Programação Dinâmica)...")
    
    trilha_otimizada_df = otimizar_trilha_nexus(
        df_cursos_disponiveis,
        CAPACIDADE_HORAS_PROFISSIONAL
    )
    
    # Apresentar Relatório de Saída
    impacto_total_alcancado = trilha_otimizada_df['Impacto_Valor'].sum()
    tempo_total_gasto = trilha_otimizada_df['Tempo_Horas'].sum()

    print("\n" + "=" * 50)
    print("RELATÓRIO DA TRILHA DE APRENDIZAGEM OTIMIZADA")
    print("=" * 50)
    print(f"Capacidade de Tempo Total: {CAPACIDADE_HORAS_PROFISSIONAL} horas")
    print("\n---Resultados da Otimização---")
    print(f"Impacto na Carreira Máximo: {impacto_total_alcancado}")
    print(f"Tempo Total Utilizado: {tempo_total_gasto} horas")
    
    print("\n---Cursos Selecionados---")
    if trilha_otimizada_df.empty:
        print("Nenhum curso pode ser selecionado com o tempo disponível.")
    else:
        # Exibe a tabela de cursos, removendo o 'ID' que é interno
        print(trilha_otimizada_df[['Nome', 'Tempo_Horas', 'Impacto_Valor']].to_string(index=False))
    print("=" * 50)