"""
 Você e sua equipe de programadores foram contratados para desenvolver um
app de vendas para uma loja que vende Açaí e Cupuaçu. Você ficou com a parte de
desenvolver a interface do cliente para retirada do produto.
A Loja possui seguinte relação:
• Tamanho P de Cupuaçu (CP) custa 9 reais e o Açaí (AC) custa 11 reais;
• Tamanho M de Cupuaçu (CP) custa 14 reais e o Açaí (AC) custa 16 reais;
• Tamanho G de Cupuaçu (CP) custa 18 reais e o Açaí (AC) custa 20 reais;

"""
nome = 'Gabriel Braga'
print(f'Bem vindo(a) a loja de açaí do {nome}')
print('-'*20, 'Cardápio', '-'*20)
print('-'*50)

valor_total = 0

while True:
    sabor = str(input('Digite o sabor desejado (CP/AC): ')).upper()
    if sabor != 'AC' and sabor != 'CP':
        print('Sabor inválido. Tente novamente.')
        break
    tam = str(input('Digite o tamanho desejado (P/M/G):')).upper()
    if tam != 'P' and tam != 'M' and tam != 'G':
        print('Tamanha inválido. Tente novamente.')
        break

    else:
        if sabor == 'AC' and tam == 'P':
            preco = 11
        elif sabor =='AC' and tam == 'M':
            preco = 16
        elif sabor == 'AC' and tam == 'G':
            preco = 20
        elif sabor == 'CP' and tam == 'P':
            preco = 9
        elif sabor == 'CP' and tam == 'M':
            preco = 14
        elif sabor == 'CP' and tam == 'G':
            preco = 18
    
    valor_total += preco

    usuario = str(input('Deseja mais alguma coisa (S/N)? ')).upper()
    if usuario == 'S':
        continue
    elif usuario == 'N':
        print(f'O valor total a ser pago é de: {valor_total}')
        break  

