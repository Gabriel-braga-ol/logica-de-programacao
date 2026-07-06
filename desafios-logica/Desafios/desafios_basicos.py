"""
============================================================
DESAFIOS BÁSICOS - Funções em Python
============================================================
Nível: Iniciante
Conteúdos: Definição de funções, parâmetros, retorno simples
============================================================
Instruções:
- Leia cada enunciado com atencão.
- Escreva sua solução abaixo de cada enunciado.
- Teste sua função chamando-a com diferentes valores.
============================================================
"""

# ------------------------------------------------------------
# DESAFIO 1: Saudação Personalizada
# ------------------------------------------------------------
# Crie uma função chamada `saudar` que receba um nome como
# parâmetro e imprima: "Olá, [nome]! Bem-vindo ao curso."
# Se nenhum nome for passado, use "Aluno" como padrão.
#
# Exemplo:
#   saudar("Maria")  -> Olá, Maria! Bem-vindo ao curso.
#   saudar()         -> Olá, Aluno! Bem-vindo ao curso.
# ------------------------------------------------------------

# Escreva sua solução abaixo:

"""
def saudacao(nome='Aluno'):
    print(f'Olá, {nome}! Bem vindo(a) ao curso')

saudacao('Gabriel')
saudacao()
"""

# ------------------------------------------------------------
# DESAFIO 2: Calculadora de Área do Retângulo
# ------------------------------------------------------------
# Crie uma função chamada `area_retangulo` que receba a base
# e a altura de um retângulo e RETORNE a área.
# Depois, fora da função, peça os valores ao usuário, chame a
# função e mostre o resultado formatado.
#
# Exemplo:
#   Digite a base: 5
#   Digite a altura: 3
#   A área do retângulo é 15.
# ------------------------------------------------------------

# Escreva sua solução abaixo:

"""
base = int(input('Digite a base: '))
altura = int(input('Digite a altura: '))

def area_retangulo():
    resp = base * altura
    print(f'A area do retângulo é: {resp}')

area_retangulo()
"""

# ------------------------------------------------------------
# DESAFIO 3: Verificador de Número
# ------------------------------------------------------------
# Crie uma função chamada `verifica_numero` que receba um
# número inteiro e RETORNE uma string dizendo se ele é:
#   - "Positivo"
#   - "Negativo"
#   - "Zero"
#
# Depois, use um laço for para testar a função com os
# valores: -5, 0, 10, -1, 7
# ------------------------------------------------------------

# Escreva sua solução abaixo:

"""
def verifica_numero(num):
    if num > 0:
        return 'Positivo'
    elif num < 0:
        return 'Negativo'
    else:
        return 'Zero'

valores = [-5, 0, 10, -1, 7]

for i in valores:
    numero = verifica_numero(i)
    print(f'{i} -', numero)
"""

# ------------------------------------------------------------
# DESAFIO 4: Conversor de Temperatura
# ------------------------------------------------------------
# Crie uma função chamada `celsius_para_kelvin` que receba uma
# temperatura em Celsius e RETORNE a temperatura em Kelvin.
# Fórmula: K = C + 273.15
#
# Crie também uma função `celsius_para_fahrenheit` que receba
# Celsius e RETORNE Fahrenheit.
# Fórmula: F = (9 * C / 5) + 32
#
# Peça uma temperatura ao usuário e mostre as duas conversões.
# ------------------------------------------------------------

# Escreva sua solução abaixo:

"""
def celsius_para_kelvin(c):
    return c + 273.15

def celsius_para_fahrenheit(c):
    x = (9 * c / 5) + 32
    return x

temp = int(input('Digite uma temperatuta: '))
print(f'Kelvin', {celsius_para_kelvin(temp)})
print(f'Fahrenheit', {celsius_para_fahrenheit(temp)})
"""

# ------------------------------------------------------------
# DESAFIO 5: Contador de Vogais
# ------------------------------------------------------------
# Crie uma função chamada `contar_vogais` que receba uma
# string e RETORNE a quantidade de vogais (a, e, i, o, u)
# presentes nela. A função deve funcionar com letras
# maiúsculas e minúsculas.
#
# Exemplo:
#   contar_vogais("Python")      -> 1
#   contar_vogais("Lógica")      -> 3
#   contar_vogais("AEIOU")       -> 5
# ------------------------------------------------------------

# Escreva sua solução abaixo:

"""
vogais = 'aeiouAEIOU'

def contar_vogais(texto):
    cont = 0
    for i in texto:
        if i in vogais:
            cont += 1
    return cont
       
print(contar_vogais('Python'))
print(contar_vogais('Logica'))
print(contar_vogais('Gabriel'))
print(contar_vogais('Adeus'))
"""

# ==================== GABARITO (opcional) ====================
# Descomente as linhas abaixo se quiser ver uma possível
# solução após tentar resolver sozinho.
# =============================================================

# def saudar(nome="Aluno"):
#     print(f"Olá, {nome}! Bem-vindo ao curso.")
#
# def area_retangulo(base, altura):
#     return base * altura
#
# b = float(input("Digite a base: "))
# h = float(input("Digite a altura: "))
# print(f"A área do retângulo é {area_retangulo(b, h)}.")
#
# def verifica_numero(n):
#     if n > 0:
#         return "Positivo"
#     elif n < 0:
#         return "Negativo"
#     else:
#         return "Zero"
#
# for valor in [-5, 0, 10, -1, 7]:
#     print(f"{valor} -> {verifica_numero(valor)}")
#
# def celsius_para_kelvin(c):
#     return c + 273.15
#
# def celsius_para_fahrenheit(c):
#     return (9 * c / 5) + 32
#
# temp = float(input("Digite a temperatura em Celsius: "))
# print(f"Kelvin: {celsius_para_kelvin(temp):.2f}")
# print(f"Fahrenheit: {celsius_para_fahrenheit(temp):.2f}")
#
# def contar_vogais(texto):
#     vogais = "aeiouAEIOU"
#     contador = 0
#     for letra in texto:
#         if letra in vogais:
#             contador += 1
#     return contador

