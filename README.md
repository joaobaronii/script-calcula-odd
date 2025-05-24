# Calculadora de Odds (Poisson)

Esta ferramenta em Python utiliza a distribuição de Poisson para calcular a probabilidade de ocorrência de um determinado número de eventos, a "odd justa" correspondente e a margem de lucro da casa de apostas. É útil para analisar apostas em eventos esportivos onde a frequência de um evento (como gols, cantos, cartões, etc.) pode ser modelada por uma média conhecida.

## Funcionalidades

O script realiza os seguintes cálculos:

1.  **Cálculo de Probabilidade (Distribuição de Poisson):**

2.  **Cálculo de Odd Justa:**

3.  **Cálculo da Margem da Casa de Apostas:**

## Detalhes das Funções

* `calcula_prob(media, ocorrencia, mais_menos)`: Retorna a probabilidade com base na média (`media`), no número de referência de ocorrências (`ocorrencia`) e no tipo de cálculo (`mais_menos`: 1 para mais de, 2 para menos de, 3 para exatamente).
* `calcula_odd(prob)`: Converte a probabilidade (`prob`) em odd.
* `calcula_margem_casa(odd_justa, odd_casa)`: Calcula a margem percentual da casa de apostas.
