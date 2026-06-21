"""
A tupla é uma estrutura de dados estática e imutável
"""

# linguagens = ('JavaScript', 'Kotlin', 'C#', 'C++', 'Python', 'Java', 'Rust', 'Dart')

# i = 0
# while linguagens[i] != 'Java':
#     i += 1

# print(f'Encontramos a linguagem Java na {i + 1}ª posição')

"""
Escreva uma função que contenha dois parâmetros. Essa função recebe
como parâmetro uma string com uma mensagem a ser impressa na tela, e outro
parâmetro como sendo uma quantidade arbitrária de números empacotados.
Dentro da função, encontre o maior dentre todos os números recebidos e
escreva na tela, dentro da função, a mensagem e o maior valor.
"""

# def maior_numero(msg, *num):
#     maior = 0
#     for numero in num:
#         if numero > maior:
#             maior = numero
#     print(msg, maior)        

# exercicio('Maior:', 5, 6, 10, 55, 12, 23)

def soma(*num):
    acumulador = 0
    print(f'Tupla: {num}')
    for numero in num:
        acumulador += numero
    return acumulador

print(soma(1,2))
print(soma(1,2,66,23,59))