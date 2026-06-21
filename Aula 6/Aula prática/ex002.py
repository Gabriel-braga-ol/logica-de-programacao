palavras = ('Python', 'Lógica', 'Linguagem', 'Programação', 'Algoritimo')

vogais = 'aeiou'

for palavra in palavras:
    print(f'\nPalavra: {palavra}')
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra, end=' ')

