import random

def gerar_cartelas(sigla):
    matriz = [[0] * 5 for _ in range(5)]

    matriz [2][2] = sigla

    col0 = random.sample(range(1,15), 5)

    col1 = random.sample(range(16, 30), 5)

    col2 = random.sample(range(31, 45), 4)

    col3 = random.sample(range(46, 60), 5)

    col4 = random.sample(range(61, 75), 5)

    for linha in range(5):
        matriz[linha][0] = col0[linha]
        matriz[linha][1] = col1[linha]
        matriz[linha][3] = col3[linha]
        matriz[linha][4] = col4[linha]

    if linha < 2:
        matriz[linha][2] = col2[linha]
    elif linha > 2:
        matriz[linha][2] = col2[linha - 1]

    return matriz

def imprimir_cartela(cartela):
    for linha in cartela:
        for valor in linha:
            if type(valor) == str:
                print(f'[{valor}]', end=' ')
            elif valor < 10:
                print(f'[0{valor}]', end=' ')
            else:
                print(f'[{valor}]', end=' ')
        print()

def sorteia_valor(sorteados):
    sorteados = []
    numeros_sorteados = random,random(1, 75)
    sorteados.append(numeros_sorteados)
    if len(numeros_sorteados) >= 75:
        return - 1
    for numero in numeros_sorteados:
        if numero not in sorteados:
            return numero



cartela = gerar_cartelas('GB')
imprimir_cartela(cartela)
