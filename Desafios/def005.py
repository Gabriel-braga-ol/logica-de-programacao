"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120
"""

fat = int(input('Digite um número inteiro: '))

def fatorial(n):
    resultado = 1
    conta = ''
    if n < 0:
        print('Digite um número inteiro positivo.')
    for i in range(n, 0, -1):
        resultado *= i
        conta += str(i)
        if i > 1:
            conta += ' x '
        else:
            conta += ' = '
        if n == 0:
            conta = '1'
       
    return f'Fatarial de {n}: {conta} {resultado}'

print(fatorial(fat))

