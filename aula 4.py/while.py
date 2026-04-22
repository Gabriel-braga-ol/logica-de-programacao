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

while True:
    nome = input('Digite o nome: ')
    if nome != 'Gabriel':
        continue
    senha = input('Digite a senha: ')
    if senha == 'cafe':
        break
print('Acesso concedido.')