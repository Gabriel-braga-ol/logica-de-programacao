# print(1+2+3+4+5)

# n1= 23 + 19 +31
# media = n1 / 3
# print(f'{media:.2f}')

# print(403//73)
# print(403%73)
# print(2**10)
# print(abs(54-57)) #valor absoluto
# print(min(34, 29, 31)) #valor minimo

# a = 3
# b = 4
# c = a * a + b * b
# print(c)

# s1 = 'ant '
# s2 = 'bat '
# s3 = 'cod '
# resp = s1 + s2 + s3
# print(resp)
# print(s1 * 10)
# print(s1 + s2 * 2 + s3 * 3)


# preco = float(input('Digite o preço do produto: '))
# desconto = int(input('Qual o desconto? '))
# valor_desconto = preco * (desconto/100)
# preco_final = preco - valor_desconto

# print(f'O valor do produto é R${preco:.2f} com o desconto de {desconto}% o produto custará R${preco_final:.2f}. O valor do desconto foi de R${valor_desconto:.2f}')

# km = int(input('Digite a quantidade de Km percorridos: '))
# dias = int(input('Por quantos dias o carro foi alugado? '))
# preco = 60 * dias + 0.15 * km

# print(f'O veículo percorreu {km}Km em {dias}dias e custou R${preco} de aluguel.')

frase = input('Digite uma frase? ')
tam = len(frase)
frase2 = frase[:int(tam/2)]

print(frase2[-2:])
