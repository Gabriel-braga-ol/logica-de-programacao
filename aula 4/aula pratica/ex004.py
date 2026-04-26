import random

print('JOGO DE ADIVINHAÇÃO (1 - 10)')

numero = random.randint(1, 11)
tentativas = 0
while True:
    usuario = int(input('AdIvinhe o número: '))
    tentativas += 1
    if usuario == numero:
        print('Parabens você ACERTOU!!')
        break
    else:
        print('Tente novamente')

print(f'Você realizou {tentativas} tentativas')