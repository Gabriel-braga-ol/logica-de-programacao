print('Valores dos ingressos: \n \n[1] menores de 3 anos - R$ 0,00 \n[2] Entre 3 e 12 anos - R$15,00 \n[3] Maiores de 12 anos - R$ 30,00\n')

total = 0
dinheiro = 0
tot_idades = 0

while True:
    idade = int(input('Qual a sua idade: '))
    if idade == 0:
        break
    total += 1
    tot_idades += idade
    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15
    
    dinheiro += ingresso

if total > 0:
    media = tot_idades / total
    print(f'O total de pessoas que compraram o ingresso foi {total}\n O valor total foi de R${dinheiro}\n A média das idades é {media}')
