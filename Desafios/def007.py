"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:

        "Telefonou para a vítima?"
        "Esteve no local do crime?"
        "Mora perto da vítima?"
        "Devia para a vítima?"
        "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".
"""
# print('-'*10, 'Interrogatório', '-'*10)
# p1 = input('Telefonou para a vítima? ').upper()
# p2 = input('Esteve no local do crime? ').upper()
# p3 = input('Mora perto da vítima? ').upper()
# p4 = input('Devia para a vítima? ').upper()
# p5 = input('Já trabalhou para a vítima? ').upper()

# resposta = []
# resposta.extend([p1,p2,p3,p4,p5])

# total_sim = 0
# # total_nao = 0

# for i in resposta:
#     if i == 'S':
#         total_sim += 1
    
# if total_sim == 0 or total_sim == 1:
#     classificacao = 'Inocente'
# elif total_sim == 2:
#     classificacao = 'Suspeito'
# elif total_sim == 3 or total_sim == 4:
#     classificacao = 'Cumplice'
# elif total_sim == 5:
#     classificacao = 'Assassino'

# print(f'Classificação: {classificacao}')        


analise = 0

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]  

for pergunta in perguntas:
    resposta = input(pergunta).upper()
    resposta = 1 if resposta == 'S' else 0
    analise += resposta

if analise == 0 or analise == 1:
    classificacao = 'Inocente'
elif analise == 2:
    classificacao = 'Suspeito'
elif analise == 3 or analise == 4:
    classificacao = 'Cumplice'
elif analise == 5:
    classificacao = 'Assassino'  

print(f'Classificação: {classificacao}')
