# n1 = int(input('Digite um número inteiro: '))
# n2 = int(input('Digite outro inteiro: '))
# if n1 > n2:
#     print(f'{n1} é maior que {n2}')
# else:
#     print(f'{n2} é maior que {n1}')

# n1 = int(input('Digite um número inteiro: '))
# # n2 = int(input('Digite outro inteiro: '))
# if n1 % 2 == 0:
#     print('É par')
# else:
#     print('É impar')

# ano_nasc = int(input('Digite o seu ano de nascimento: '))
# ano_atual = int(input('Em que ano estamos? '))
# idade = ano_atual - ano_nasc
# print(f'Você tem {idade} anos de idade')

# if idade > 18:
#     print('Você já é maior de idade')
# else:
#     print('Você ainda é de menor')

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# n3 = float(input('Digite a terceira nota: '))
# media = (n1 + n2 + n3) / 3
# if media >= 7:
#     print(f'Sua nota foi {media}')
#     print(f'PARABÉNS!! Você foi aprovado!')
# else:
#     print(f'Sua nota foi {media}')
#     print(f'Você foi reprovado!')

print('Escolha umas das opções: \n[1]Maçã \n[2]Banana \n[3]Laranja \n')
usuario = int(input('Opção: '))
qtd = int(input('Quantas unidades deseja? '))
if usuario == 1:
    pagar = qtd * 2.3
    print(f'Você comprou {qtd} de maçã. O valor total fica R${pagar}')
elif usuario == 2:
    pagar = qtd / 1.85
    print(f'Você comprou {qtd} de banana. O valor total fica R${pagar}')
elif usuario == 3:
    pagar = qtd * 3.6
    print(f'Você comprou {qtd} de laranja. O valor total fica R${pagar}')
else:
    print('Produto inexistente')
    