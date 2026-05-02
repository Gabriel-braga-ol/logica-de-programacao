# n = int(input('Digite um número: '))

# def fatorial(n):
#     """
#     Calcula o fatorial de um número inteiro positivo fornecido pelo usuário
#     """
#     if n < 0:
#         print('Digite um número positivo')
#     resultado = 1
#     conta = ''
#     for i in range(n, 0, -1):
#         resultado *= i
#         conta += str(i)
#         if i > 1:
#             conta += ' x ' 
#         else:
#             conta += ' = '
#         if n == 0:
#             conta = '1'
#     return f'Fatorial de {n}: {conta} {resultado}'

# print(fatorial(n))
# help(fatorial)

def fatorial(n):
    """
    Calcula o fatorial de um número inteiro positivo
    """
    if n < 0:
        return 'Não existe fatorial de número negativo'
    fat = 1
    if n == 0:
        return f'Fatoria de 0 é igual a {fat}'
    conta = ''
    for i in range(n, 0, -1):
        fat *= i
        conta += str(i)
        if i > 1:
            conta += ' x '
        else:
            conta += ' = '
    return f'Fatorial de {n}: {conta} {fat}'

x = int(input('Digite um número inteiro: '))
print(f'{fatorial(x)}')
help(fatorial)