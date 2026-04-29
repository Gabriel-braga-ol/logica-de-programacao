"""
============================================================
DESAFIOS AVANÇADOS - Funções em Python
============================================================
Nível: Avançado
Conteúdos: Escopo global/local, *args, múltiplas funções,
           refatoração, modularização
============================================================
Instruções:
- Leia cada enunciado com atenção.
- Escreva sua solução abaixo de cada enunciado.
- Teste sua função chamando-a com diferentes valores.
============================================================
"""

# ------------------------------------------------------------
# DESAFIO 1: Estatísticas com *args
# ------------------------------------------------------------
# Crie uma função chamada `estatisticas` que receba qualquer
# quantidade de números usando *args e RETORNE um dicionário
# com as seguintes informações:
#   - "maior": maior número
#   - "menor": menor número
#   - "media": média aritmética
#   - "quantidade": quantidade de números
#
# Se nenhum número for passado, retorne None.
#
# Exemplo:
#   estatisticas(10, 5, 8, 20)
#   -> {"maior": 20, "menor": 5, "media": 10.75, "quantidade": 4}
# ------------------------------------------------------------

# Escreva sua solução abaixo:




# ------------------------------------------------------------
# DESAFIO 2: Caixa Eletrônico
# ------------------------------------------------------------
# Crie um sistema de caixa eletrônico usando múltiplas
# funções. O usuário deve poder:
#   - Ver saldo
#   - Depositar
#   - Sacar
#   - Sair
#
# Regras:
#   - Use uma variável global `saldo` iniciada em 0.
#   - Crie funções: ver_saldo(), depositar(valor), sacar(valor)
#   - Não permita saque maior que o saldo.
#   - Não permita valores negativos.
#   - Use um laço while para o menu.
#
# Obs: lembre-se de usar `global` quando necessário.
# ------------------------------------------------------------

# Escreva sua solução abaixo:




# ------------------------------------------------------------
# DESAFIO 3: Refatoração de Código
# ------------------------------------------------------------
# O código abaixo funciona, mas está muito repetitivo e
# desorganizado. Refatore-o criando funções adequadas.
#
# CÓDIGO ORIGINAL (não altere, apenas analise):
# -------------------------------------------------
# a1 = float(input("Nota 1 do aluno A: "))
# a2 = float(input("Nota 2 do aluno A: "))
# a3 = float(input("Nota 3 do aluno A: "))
# media_a = (a1 + a2 + a3) / 3
# if media_a >= 7:
#     status_a = "Aprovado"
# else:
#     status_a = "Reprovado"
# print(f"Aluno A - Média: {media_a:.2f} - {status_a}")
#
# b1 = float(input("Nota 1 do aluno B: "))
# b2 = float(input("Nota 2 do aluno B: "))
# b3 = float(input("Nota 3 do aluno B: "))
# media_b = (b1 + b2 + b3) / 3
# if media_b >= 7:
#     status_b = "Aprovado"
# else:
#     status_b = "Reprovado"
# print(f"Aluno B - Média: {media_b:.2f} - {status_b}")
#
# c1 = float(input("Nota 1 do aluno C: "))
# c2 = float(input("Nota 2 do aluno C: "))
# c3 = float(input("Nota 3 do aluno C: "))
# media_c = (c1 + c2 + c3) / 3
# if media_c >= 7:
#     status_c = "Aprovado"
# else:
#     status_c = "Reprovado"
# print(f"Aluno C - Média: {media_c:.2f} - {status_c}")
# -------------------------------------------------
#
# Sua tarefa: Crie uma função `processar_aluno(nome)` que
# faça tudo de forma organizada e sem repetição.
# Depois, use um laço for para processar os alunos A, B e C.
# ------------------------------------------------------------

# Escreva sua solução abaixo:




# ------------------------------------------------------------
# DESAFIO 4: Soma Dinâmica com *args
# ------------------------------------------------------------
# Crie uma função chamada `soma_ponderada` que receba:
#   - peso: um valor numérico (padrão = 1)
#   - *valores: qualquer quantidade de números
#
# A função deve RETORNAR a soma de todos os valores
# multiplicados pelo peso.
#
# Exemplo:
#   soma_ponderada(2, 5, 10, 3)
#   -> (5*2) + (10*2) + (3*2) = 36
#
#   soma_ponderada(3, 1, 2)
#   -> (1*3) + (2*3) = 9
#
#   soma_ponderada(5, 10)
#   -> 10 * 5 = 50
#
#   soma_ponderada()
#   -> 0 (nenhum valor)
# ------------------------------------------------------------

# Escreva sua solução abaixo:




# ------------------------------------------------------------
# DESAFIO 5: Contador de Palavras
# ------------------------------------------------------------
# Crie uma função chamada `analisar_frase` que receba uma
# string e RETORNE um dicionário com:
#   - "palavras": quantidade de palavras
#   - "caracteres": quantidade de caracteres (sem espaços)
#   - "mais_comum": a letra que mais aparece (ignorar espaços)
#   - "maiusculas": quantidade de letras maiúsculas
#
# Dica: use .split() para separar palavras, e um laço para
# contar as letras.
#
# Exemplo:
#   analisar_frase("O Rato Roeu")
#   -> {
#       "palavras": 3,
#       "caracteres": 9,
#       "mais_comum": "o",
#       "maiusculas": 2
#      }
# ------------------------------------------------------------

# Escreva sua solução abaixo:




# ==================== GABARITO (opcional) ====================
# Descomente as linhas abaixo se quiser ver uma possível
# solução após tentar resolver sozinho.
# =============================================================

# def estatisticas(*args):
#     if not args:
#         return None
#     return {
#         "maior": max(args),
#         "menor": min(args),
#         "media": sum(args) / len(args),
#         "quantidade": len(args)
#     }
#
# saldo = 0
#
# def ver_saldo():
#     global saldo
#     print(f"Saldo atual: R${saldo:.2f}")
#
# def depositar(valor):
#     global saldo
#     if valor < 0:
#         print("Valor inválido!")
#         return
#     saldo += valor
#     print(f"Depositado: R${valor:.2f}")
#
# def sacar(valor):
#     global saldo
#     if valor < 0:
#         print("Valor inválido!")
#         return
#     if valor > saldo:
#         print("Saldo insuficiente!")
#         return
#     saldo -= valor
#     print(f"Sacado: R${valor:.2f}")
#
# while True:
#     print("\n[1] Ver Saldo")
#     print("[2] Depositar")
#     print("[3] Sacar")
#     print("[4] Sair")
#     opcao = input("Opção: ")
#     if opcao == "1":
#         ver_saldo()
#     elif opcao == "2":
#         depositar(float(input("Valor: R$")))
#     elif opcao == "3":
#         sacar(float(input("Valor: R$")))
#     elif opcao == "4":
#         print("Saindo...")
#         break
#
# def processar_aluno(nome):
#     n1 = float(input(f"Nota 1 do aluno {nome}: "))
#     n2 = float(input(f"Nota 2 do aluno {nome}: "))
#     n3 = float(input(f"Nota 3 do aluno {nome}: "))
#     media = (n1 + n2 + n3) / 3
#     status = "Aprovado" if media >= 7 else "Reprovado"
#     print(f"Aluno {nome} - Média: {media:.2f} - {status}")
#
# for aluno in ["A", "B", "C"]:
#     processar_aluno(aluno)
#
# def soma_ponderada(peso=1, *valores):
#     return sum(v * peso for v in valores)
#
# print(soma_ponderada(2, 5, 10, 3))
# print(soma_ponderada(3, 1, 2))
# print(soma_ponderada(5, 10))
# print(soma_ponderada())
#
# def analisar_frase(frase):
#     palavras = frase.split()
#     sem_espacos = frase.replace(" ", "")
#     caracteres = len(sem_espacos)
#
#     mais_comum = ""
#     max_qtd = 0
#     for letra in sem_espacos.lower():
#         qtd = sem_espacos.lower().count(letra)
#         if qtd > max_qtd:
#             max_qtd = qtd
#             mais_comum = letra
#
#     maiusculas = sum(1 for c in frase if c.isupper())
#
#     return {
#         "palavras": len(palavras),
#         "caracteres": caracteres,
#         "mais_comum": mais_comum,
#         "maiusculas": maiusculas
#     }
#
# print(analisar_frase("O Rato Roeu"))

