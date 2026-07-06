"""
Faça um programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""


"""
domingo = 1
segunda = 2
terca = 3
quarta = 4
quinta = 5
sexta = 6
sabado = 7

while True:
    usuario = int(input('Digite um número para exibir o dia da semana: '))
    if usuario not in [1,2,3,4,5,6,7]:
        print('Opção inválida. Tente novamente.')
        continue
    else:
        if usuario == 1:
            print('DOMINGO')
        elif usuario == 2:
            print('SEGUNDA')
        elif usuario == 3:
            print('TERÇA')
        elif usuario == 4:
            print('QUARTA')
        elif usuario == 5:
            print('QUINTA')
        elif usuario == 6:
            print('SEXTA')
        elif usuario == 7:
            print('SABADO')
    break
"""

dias_semana = {
    '1': 'Domingo',
    '2': 'Segunda',
    '3': 'Terça',
    '4': 'Quarta',
    '5': 'Quinta',
    '6': 'Sexta',
    '7': 'Sábado'
}

usuario = str(input('Digite um número para exibir o dia da semana: '))
if usuario not in dias_semana:
    print('Opção inválida.Tente novamente.')
else:
    print(dias_semana[usuario])