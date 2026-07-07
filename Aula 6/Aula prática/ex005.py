def menu():
    return 'Escolha uma das opções: \n[1]Maçã \n[2]Laranja \n[3]Banana'

menu = menu()

print(menu)

produto = int(input('Digite o número do produto desejado: '))
qtd = int(input('Digite a quantidade desejada: '))

match (produto):
    case 1:
        pagar = qtd * 2.3
        print(f'Você comprou {qtd} Maçã(s) e o valor total é R$ {pagar:.2f}')
    case 2:
        pagar = qtd * 3.5
        print(f'Você comprou {qtd} Laranja(s) e o valor total é R$ {pagar:.2f}')
    case 3:
        pagar = qtd * 1.8
        print(f'Você comprou {qtd} Banana(s) e o valor total é R$ {pagar:.2f}')
    case _:
        print('Opção inválida')
