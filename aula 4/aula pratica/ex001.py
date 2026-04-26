# x = 3
# while x != 13:
#     print(x)
#     x += 1

# for i in range(3, 13, 1):
#     print(i)

# x = 0
# while x < 10:
#     print(x)
#     x += 2

# for i in range(0, 9, 2):
#     print(i)

print('Preços dos salgados: \n \n[1]Coxina - R$ 5,00 \n[2]Pastel - R$ 7,00 \n[3]Café - R$ 4,00 \n[4]Suco - R$ 6,00 \n[5]Sair\n')

total = 0

while True:
    opcao = int(input('Escolha uma opção: '))
    if opcao == 5:
        print('Encerrando o programa')
        break
    
    if opcao == 1:
        qtd = int(input('Selecione a quantidade: '))
        total += qtd * 5     
    elif opcao == 2:
        qtd = int(input('Selecione a quantidade: '))
        total += qtd * 7      
    elif opcao == 3:
        qtd = int(input('Selecione a quantidade: '))
        total += qtd * 4 
    elif opcao == 4:
        qtd = int(input('Selecione a quantidade: '))
        total += qtd * 6       
    else:
        print('Escolha uma opção válida.')
    

print(f'O valor total do pedido fica R$ {total}')

