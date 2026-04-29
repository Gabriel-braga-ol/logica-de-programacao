"""
============================================================
DESAFIOS INTERMEDIÁRIOS - Funções em Python
============================================================
Nível: Intermediário
Conteúdos: Condicionais, laços, valores padrão, argumentos
           nomeados, múltiplos parâmetros
============================================================
Instruções:
- Leia cada enunciado com atenção.
- Escreva sua solução abaixo de cada enunciado.
- Teste sua função chamando-a com diferentes valores.
============================================================
"""

# ------------------------------------------------------------
# DESAFIO 1: Calculadora de IMC
# ------------------------------------------------------------
# Crie uma função chamada `calcular_imc` que receba peso (kg)
# e altura (m), e RETORNE o IMC.
# Fórmula: IMC = peso / (altura ** 2)
#
# Crie outra função chamada `classificar_imc` que receba o
# IMC e RETORNE a classificação:
#   - Menor que 18.5: "Abaixo do peso"
#   - De 18.5 a 24.9: "Peso normal"
#   - De 25.0 a 29.9: "Sobrepeso"
#   - 30.0 ou maior:  "Obesidade"
#
# Peça peso e altura ao usuário, calcule e mostre o resultado
# completo com a classificação.
# ------------------------------------------------------------

# Escreva sua solução abaixo:

"""
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

    
def classificar_imc(imc):
    if imc < 18.5:
        return 'Você está abaixo do peso'
    elif imc > 18.5 and imc < 24.9:
        return 'Você está com peso normal'
    elif imc > 25.0 and imc < 29.9:
        return 'Você está com sobrepeso'
    else:
        return 'Você está co obesidade'

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = calcular_imc(peso, altura)
print(f'Seu imc é: {imc:.2f} \n{classificar_imc(imc)}')
"""

# ------------------------------------------------------------
# DESAFIO 2: Fatorial
# ------------------------------------------------------------
# Crie uma função chamada `fatorial` que receba um número
# inteiro não negativo e RETORNE o fatorial desse número.
# Fatorial de 5 = 5 * 4 * 3 * 2 * 1 = 120
# Fatorial de 0 = 1
#
# Valide se o número é negativo. Se for, retorne uma
# mensagem de erro.
#
# Use um laço for ou while dentro da função.
# ------------------------------------------------------------

# Escreva sua solução abaixo:




# ------------------------------------------------------------
# DESAFIO 3: Tabuada Personalizada
# ------------------------------------------------------------
# Crie uma função chamada `tabuada` que receba:
#   - numero: o número da tabuada
#   - inicio: valor inicial do intervalo (padrão = 1)
#   - fim:    valor final do intervalo   (padrão = 10)
#
# A função deve imprimir a tabuada do número no intervalo
# especificado, usando argumentos nomeados.
#
# Exemplo:
#   tabuada(7, inicio=5, fim=8)
#   7 x 5 = 35
#   7 x 6 = 42
#   7 x 7 = 49
#   7 x 8 = 56
# ------------------------------------------------------------

# Escreva sua solução abaixo:




# ------------------------------------------------------------
# DESAFIO 4: Juros Simples e Compostos
# ------------------------------------------------------------
# Crie uma função `juros_simples` que receba:
#   capital, taxa (em % ao mês), tempo (meses)
# e RETORNE o montante final.
# Fórmula: M = capital * (1 + (taxa/100) * tempo)
#
# Crie uma função `juros_compostos` com os mesmos parâmetros,
# mas usando a fórmula: M = capital * (1 + taxa/100) ** tempo
#
# Peça os dados ao usuário e mostre a diferença entre os dois
# tipos de juros após 12 meses.
# ------------------------------------------------------------

# Escreva sua solução abaixo:




# ------------------------------------------------------------
# DESAFIO 5: Validação de Senha
# ------------------------------------------------------------
# Crie uma função chamada `validar_senha` que receba uma
# string (senha) e RETORNE True se a senha for forte, ou
# False caso contrário.
#
# Critérios para senha forte:
#   - Mínimo 8 caracteres
#   - Pelo menos 1 letra maiúscula
#   - Pelo menos 1 letra minúscula
#   - Pelo menos 1 número
#
# Dica: use os métodos de string .isupper(), .islower(),
# .isdigit() e laços para verificar cada caractere.
# ------------------------------------------------------------

# Escreva sua solução abaixo:




# ==================== GABARITO (opcional) ====================
# Descomente as linhas abaixo se quiser ver uma possível
# solução após tentar resolver sozinho.
# =============================================================

# def calcular_imc(peso, altura):
#     return peso / (altura ** 2)
#
# def classificar_imc(imc):
#     if imc < 18.5:
#         return "Abaixo do peso"
#     elif imc <= 24.9:
#         return "Peso normal"
#     elif imc <= 29.9:
#         return "Sobrepeso"
#     else:
#         return "Obesidade"
#
# peso = float(input("Digite seu peso (kg): "))
# altura = float(input("Digite sua altura (m): "))
# imc = calcular_imc(peso, altura)
# print(f"Seu IMC é {imc:.2f} ({classificar_imc(imc)})")
#
# def fatorial(n):
#     if n < 0:
#         return "Erro: número negativo"
#     resultado = 1
#     for i in range(1, n + 1):
#         resultado *= i
#     return resultado
#
# print(f"Fatorial de 5: {fatorial(5)}")
# print(f"Fatorial de 0: {fatorial(0)}")
#
# def tabuada(numero, inicio=1, fim=10):
#     for i in range(inicio, fim + 1):
#         print(f"{numero} x {i} = {numero * i}")
#
# tabuada(7, inicio=5, fim=8)
#
# def juros_simples(capital, taxa, tempo):
#     return capital * (1 + (taxa / 100) * tempo)
#
# def juros_compostos(capital, taxa, tempo):
#     return capital * (1 + taxa / 100) ** tempo
#
# c = float(input("Capital: R$ "))
# t = float(input("Taxa (% ao mês): "))
# print(f"Juros simples em 12 meses: R${juros_simples(c, t, 12):.2f}")
# print(f"Juros compostos em 12 meses: R${juros_compostos(c, t, 12):.2f}")
#
# def validar_senha(senha):
#     if len(senha) < 8:
#         return False
#     tem_maiuscula = False
#     tem_minuscula = False
#     tem_numero = False
#     for caractere in senha:
#         if caractere.isupper():
#             tem_maiuscula = True
#         elif caractere.islower():
#             tem_minuscula = True
#         elif caractere.isdigit():
#             tem_numero = True
#     return tem_maiuscula and tem_minuscula and tem_numero
#
# print(validar_senha("Senha123"))  # True
# print(validar_senha("senha"))     # False

