INTEGRANTES:
RM554583 Leonardo Ceschim Taschin
RM555152 Willian Moreira

# NEXUS: Otimizador de Trilhas de Aprendizagem (Global Solution)

Este projeto é uma solução para a disciplina de Dynamic Programming, com o tema "Future at Work". Ele apresenta o **NEXUS**, uma plataforma teórica de upskilling/reskilling que utiliza IA para criar trilhas de aprendizagem personalizadas.

O núcleo deste trabalho é a aplicação de **Programação Dinâmica** para resolver um problema de otimização dentro da plataforma NEXUS.

## Problemática: Otimização da Trilha de Aprendizagem

Modelamos o desafio do usuário como o **Problema da Mochila 0/1 (Knapsack Problem)**:

* **Contexto:** Um profissional tem um tempo total limitado (Capacidade da Mochila) que pode dedicar aos estudos (ex: 25 horas).
* **Itens:** A plataforma NEXUS sugere um conjunto de cursos, cada um com um "peso" e "valor".
* **Peso (Weight):** O `Tempo_Horas` necessário para completar um curso.
* **Valor (Value):** O `Impacto_Valor` (de 0 a 100) que o curso traz para a carreira do profissional.

### Formulação Formal do Problema

* **Entrada:**
    1.  Uma lista de $N$ cursos.
    2.  Cada curso $i$ tem um peso $p_i$ (Tempo_Horas) e um valor $v_i$ (Impacto_Valor).
    3.  Uma capacidade total $C$ (Tempo total disponível do profissional).

* **Objetivo (Maximização):**
    Encontrar um subconjunto de cursos $S$ que maximize o valor total (Impacto na Carreira), sem que a soma dos pesos (Tempo) ultrapasse a capacidade $C$.

    $$\text{Maximizar} \sum_{i \in S} v_i$$
    $$\text{Sujeito a} \sum_{i \in S} p_i \le C$$

* **Saída:**
    1.  O valor máximo de "Impacto na Carreira" que pode ser alcançado.
    2.  O tempo total que será gasto.
    3.  A lista de cursos selecionados que compõem essa trilha otimizada.

## Solução Técnica

O problema da Mochila 0/1 é resolvido usando Programação Dinâmica com a abordagem **Top-Down (Recursão com Memoização)**.

* **Estrutura de Dados:** Os cursos são carregados em um **Pandas DataFrame** para fácil manipulação e visualização.
* **Algoritmo de Ordenação:** (Opcional para análise) Foi implementada uma versão recursiva do **Merge Sort** para demonstrar a ordenação dos dados.
* **Algoritmo de Otimização:** A função principal `resolver_mochila_memo` utiliza recursão para explorar todas as combinações (incluir ou não incluir um curso) e armazena resultados já calculados em um dicionário (memo) para evitar recálculos, garantindo a eficiência da PD.

## Como Executar o Projeto

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/WillianMoreiraBFP/GS-2025-2-Semestre.git
    cd GS-2025-2-Semestre
    ```

2.  **Crie um ambiente virtual (Recomendado):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    O projeto requer a biblioteca `pandas`.
    ```bash
    pip install pandas
    ```

4.  **Execute o script:**
    ```bash
    python nexus.py
    ```

O script irá carregar os dados, executar o otimizador e imprimir no terminal o relatório final com a trilha de cursos recomendada, o impacto máximo e o tempo total.
