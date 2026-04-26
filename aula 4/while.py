# x = 1
# while x <= 5:
#     print(x)
#     x = x + 1

# contador = 0

# while contador < 100:
#     contador += 1
#     if contador == 10:
#         continue
#     if contador >=20 and contador <= 30:
#         print('Não mostrou o', contador)
#         continue
#     print(contador)
#     if contador == 40:
#         break
# print('FIM')

# frase = 'O python é uma linguagem de programação '\
#     'multiparadigma. '\
#     'Python foi criado por Guido Van Rossum.' 
# # O \ é usado para quebrar linha

# i = 0
# qtd_apareceu_mais_vezes = 0
# letra_apareceu_mais_vezes = ''
# while i < len(frase):
#     letra_atual = frase[i]

#     if letra_atual == ' ':
#         i += 1
#         continue
    
#     quantas_vezes_letra_atual_apareceu = frase.count(letra_atual)

#     if qtd_apareceu_mais_vezes < quantas_vezes_letra_atual_apareceu:
#         qtd_apareceu_mais_vezes = quantas_vezes_letra_atual_apareceu
#         letra_apareceu_mais_vezes = letra_atual
    
    

#     i += 1

# print('A letra que apareceu mais vezes foi '
#       f'"{letra_apareceu_mais_vezes}" que apareceu '
#       f'{qtd_apareceu_mais_vezes}x')

# v_inicial = int(input('Digite um valor inicial: '))
# v_final = int(input('Digite um valor final: '))

# x = v_inicial
# while x <= v_final:
#     if x % 2 == 0:
#         print(x)
#     x = x + 1 # variavel contadora

# soma = 0
# cont = 1
# while cont <= 5:
#     x = float(input(f'Digite a {cont} nota: '))
#     soma += x
#     cont += 1
# media = soma / 5
# print(f'A média final é {media}')

# x = int(input('Digite um valor maior do que 0: '))
# while x <= 0:
#     x = int(input('Digite um valor maior do que 0: '))        
# print(f'Você digitou {x}. encerrando o programa')

# while True:
#     x = input('Digite algo: ')
#     if x == 'sair':
#         break
# print('Encerrando o programa...')

# while True:
#     nome = input('Digite o nome: ')
#     if nome != 'Gabriel':
#         continue
#     senha = input('Digite a senha: ')
#     if senha == 'cafe':
#         break
# print('Acesso concedido.')

# v_inicial = int(input('Digite um valor inicial: '))
# v_final = int(input('Digite um valor final: '))

# x = v_inicial
# while x <= v_final:
#     if x % 3 == 0:
#         print(x)
#     x = x + 1 # variavel contadora

# x = int(input('Digite um número: '))
# cont = 1
# while cont <= 10:
#     resp = x * cont
#     print(f'{x} x {cont} = {resp}')
#     cont += 1

# x = int(input('Digite um número: '))
# y = int(input('Digite outro número: '))
# multi = 0
# cont = 1
# while cont <= x:
#     multi = multi + y
#     cont += 1
#     print(f'O resultado da multiplicação é {multi}')

# inicial = int(input('Digite um número: '))
# final = int(input('Digite outro número: '))
# qtd_positivos = 0
# qtd_pares = 0
# qtd_impares = 0
# soma_positivos = 0
# soma_pares = 0
# soma_impares = 0

# i = inicial # Varaiavel contadora ou de controle
# if inicial < final:
#     while i <= final: # Percorre todos os núemros do intervalo
#         if i > 0:
#             qtd_positivos += 1
#             soma_positivos += i # Soma o valor de i na soma dos positivos
#         if i % 2 == 0:
#             qtd_pares += 1
#             soma_pares += i
#         else:
#             qtd_impares += 1
#             soma_impares += i
#         i += 1
# media_positivo = soma_positivos / qtd_positivos
# media_par = soma_pares / qtd_pares
# media_impares = soma_impares / qtd_impares

# print(f'Números positivos e inteiros: {qtd_positivos},')
# print(f'Média dos números positivos e inteiros: {media_positivo},')
# print(f'Números pares: {qtd_pares},')
# print(f'Média dos números pares: {media_par},')
# print(f'Números impares: {qtd_impares},')
# print(f'Média dos números impares: {media_impares},')


# soma = 0
# qtd_num = 0
# x = 0
# while True:
#     x = int(input('Digite um número inteiro: '))
#     if x < 0:
#         continue
#     if not x:
#         break
#     soma += x
#     qtd_num += 1
# media = soma / qtd_num
# print(f'A média dos númeos é igual a: {media}')

# i = 3 
# while i != 0:
#     print('Miau')
#     i -= 1

