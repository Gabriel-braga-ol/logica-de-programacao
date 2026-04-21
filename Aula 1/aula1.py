# nome = 'Olá, mundo!'
# print(nome)

# print('O resultado da equação 10*(5 + 7)/4 é:', 10*(5 + 7)/4)

# s1 = 'Lógica de programação e '
# s2 = 'algoritimo'
# resp = s1 + s2
# print(resp)

# print('A', '-'*10, 'B')

# nota = 8.9
# s1 = 'Você tirou %.2f na disciplina' %nota
# # print(s1)

# print(f'Você tirou {nota} na disciplina')

# s1 = 'Lógica de programação e algoritmo'
# print(len(s1))
# print(s1[24:])

# idade = input('Qual sua idade? ')
# print(idade)

# /*Exercicios*/

# n1 = int(input('Digite um número inteiro: '))
# n2 = int(input('Digite outro inteiro: '))
# resp = n1 + n2
# print('A soma dos dois números é:', resp)

# d = int(input('Quantos dias? '))
# h = int(input('Quantos horas? '))
# m = int(input('Quantos minutos? '))
# s = int(input('Quantos segundos? '))

# total = s + (m*60) + (h*60*60) + (d*24*60*60)
# print(f'O total de segundos é: {total}')

# preco = float(input('Digite o preço do produto: '))
# desconto = int(input('Qual o desconto? '))
# valor_desconto = preco * (desconto/100)
# preco_final = preco - valor_desconto

# print(f'O valor do produto é {preco} com o desconto de {desconto}% o produto custará R${preco_final}. O valor do desconto foi de {valor_desconto}')

c = float(input('Digite uma temperatura de celsius: '))
f = (9*c/5) + 32

print(f'{c:.0f}° celsius convertido para Fahrenheit é igual a {f:.0f}°')