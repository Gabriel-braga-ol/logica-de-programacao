# if (2 + 2 < 4):
#     print('Verdadeiro')

# x = 2
# y = 2
# z = 2 + 2 < 4
# print(z)

# if (1387 % 19 == 0):
#     print('Verdadeiro')

# if (31 % 2 == 0):
#     print('Verdadeiro')

# dano = 13
# escudo = 0

# if dano > 10 and escudo == 0:
#     print('Voce está morto')

# norte = True
# sul = False
# leste = False
# oeste = False

# if norte == True or sul == True or leste == True or oeste == True:
#     print('Você escapou!')

# cima = True
# baixo = False
# if cima == True and baixo == True:
#     print('Decida-se')
# else:
#     print('Você escolheu um caminho!')

# a = int(input('Digite o primeiro lado: '))
# b = int(input('Digite o segundo lado: '))
# c = int(input('Digite o terceiro lado: '))
# if (a > 0 and b > 0 and c > 0) and (a + b > c and a + c > b and b + c > a):
#     if a == b == c:
#         print('Isso é triângulo equilátero!')
#     elif a == b or b == c or a == c:
#         print('Isso é um triângulo isósceles!')
#     else:
#         print('Isso é um triângulo escaleno!')
# else:
#     print('Não é um triângulo!')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print('Escolha uma das opções (ou pressione qualquer tecla para sair): \n[1] adição \n[2] subtração \n[3] multiplicação \n[4] divisão')

opcao = input('Escolha uma opção: ')

if opcao == 1:
    print('A soma dos valores é igual a:', n1 + n2)
elif opcao == 2:
    print('A subtração dos valores é igual a:', n1 - n2)
elif opcao == 3:
    print('A multiplicação dos valores é igual a:', n1 * n2)
elif opcao == 4:
    print('A divisão dos valores é igual a:', n1 / n2)
else:
    print('Encerrando o programa...')
    