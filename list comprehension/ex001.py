# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

# print(list(range(10)))

import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# lista = []
# for numero in range(10):
#     lista.append(numero)
# # print(lista)

# lista =[
#     numero * 2
#     for numero in range(10)
# ]
# print(list(range(10)))
# print(lista)

# Mapeamento de dadso em list comprehension
produtos = [
    {'nome': 'p1', 'preço': 20},
    {'nome': 'p2', 'preço': 10},
    {'nome': 'p3', 'preço': 30},
]

novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.05}
    if produto['preço'] > 20 else {**produto} # Aumentando o preço do produto se for maior que 20 reais
    for produto in produtos
]
# print(novos_produtos)
# print(*novos_produtos, sep='\n') # O '*' serve para desempacotar
# p(novos_produtos)

# lista = [n for n in range(10) if n < 5]
novos_produtos = [
    {**produto, 'preço': produto['preço'] * 1.05}
    if produto['preço'] > 20 else {**produto} # Aumentando o preço do produto se for maior que 20 reais
    for produto in produtos
    if (produto['preço'] >= 20 and produto['preço'] * 1.05) > 10 # só serão incluindo produtos maiores que 10
]
p(novos_produtos)