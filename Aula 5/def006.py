# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def multiplicar(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplicaçao = multiplicar(10, 2, 5, 9, 7)
print(multiplicaçao)

def par_impar(n):
    if n % 2 == 0:
        return f'{n} é par'
    else:
        return f'{n} é impar'
    
print(par_impar(3))
