"""
Retorno de valores das funções (return)
Print e return são coisas diferentes!!!!
return só funciona com funções e metodos

args - argumentos não nomeados
*args (empacotamento e desempacotamento)
"""
x, y, *resto = 1,2,3,4
print(x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for i in args:
        total += i
    return total

soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)
