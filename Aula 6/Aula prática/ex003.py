import random

def vencedor(jogador1, jogador2):
    global empate, v1, v2
    if jogador1 == 1:
        if jogador2 == 1:
            empate += 1
        elif jogador2 == 2:
            v2 += 1
        elif jogador2 == 3:
            v1 += 1
    if jogador1 == 2:
        if jogador2 == 2:
            empate += 1        
        elif jogador2 == 1:
            v1 += 1
        elif jogador2 == 3:
            v2 += 1
    if jogador1 == 3:
        if jogador2 == 3:
            empate += 1
        elif jogador2 == 1:
            v2 += 1
        elif jogador2 == 2:
            v1 += 1
    resultados = [v1, v2, empate]
    return resultados

print('-'*10, 'JOKENPO', '-'*10)
print('[1]pedra \n[2]papel \n[3]tesoura')

jogadas = []
resultado = []
empate = 0
v1 = 0
v2 = 0

while True:
    usuario = int(input('Escolha a sua jogada: '))
    if usuario not in [1, 2, 3]:
        print('Escolha um número de 1 a 3.')
        continue
  
    
    computador = random.randint(1, 3)
    jogadas.append([usuario, computador])
    resultados = vencedor(usuario, computador)

for jogada in jogadas:
    for dado in jogada:
        print(dado, end='')
    print()

print(f'Resultados do usuário: {resultados[0]}')
print(f'Resultados do computador: {resultados[1]}')
print(f'Empates: {resultados[3]}')