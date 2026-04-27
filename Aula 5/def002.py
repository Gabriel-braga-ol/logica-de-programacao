"""
argumento nomeado - tem nome com sinal de igual
argumento não nomeado - recebe apenas o argumento (valor)
"""

# def soma(x, y, z):   #argumentos posicional
#     print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

# # print(soma(2,2)) - redundante - retorna none
# soma(5,2,1)
# soma(y=5, z=2, x=1)

# def borda(s1):
#     tam = len(s1)
#     if tam:
#         print('+','-' * tam,'+')
#         print('|', s1, '|')
#         print('+','-' * tam,'+')

# borda('gabriel')
# borda('Logica de programação')

# def contador(fim, inicio=0, passo=1):
#     for i in range(inicio, fim+1, passo):
#         print(f'{i}', end=' ')
#     print('\n')

# contador(20, 10, 1)
# contador(20)

def crescente(x=0, y=0, z=0):
    if x and y and z:
        if x > y and x > z:
            if y > z:
                print(f'Ordem crescente: {z}, {y}, {x}')
            else:
                print(f'Ordem crescente: {y}, {z}, {x}')
        elif y > x and y > z:
            if x > z:
                print(f'Ordem crescente: {z}, {x}, {y}')
            else:
                print(f'Ordem crescente: {x}, {z}, {y}')
        elif z > x and z > y:
            if x > y:
                print(f'Ordem crescente: {y}, {x}, {z}')
            else:
                print(f'Ordem crescente: {x}, {y}, {z}')
# crescente(10, 20, 5)
v1 = int(input('Digite um valor: '))
v2 = int(input('Digite um valor: '))
v3 = int(input('Digite um valor: '))

crescente(v1, v2, v3)