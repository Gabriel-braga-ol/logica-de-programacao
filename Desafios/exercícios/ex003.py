nome = 'Gabriel Braga'
print(f'Bem vindo(a) a copiadora do {nome}\n')

print('Serviços disponibilizados: \nDIG - Digitalização \nICO - Impressão colorida \nIPB - Impressão preto e branco \nFOT - Fotocópia')

def escolha_servico():
    while True:
        servico = str(input('Digite o serviço desejado: ')).upper()

        if servico == 'DIG':
            return 1.10
        elif servico == 'ICO':
            return 1.00
        elif servico == 'IPB':
            return 0.40
        elif servico == 'FOT':
            return 0.20
        else:
            print('Selecione um opção válida.')

def num_pagina():
    while True:
        try:
            pagina = int(input('Digite o número de páginas: '))
            if pagina > 20000:
                return 'Não aceitamos pedidos com essa quantidade de páginas'
            else:
                if pagina < 20:
                    return 'O desconto não será aplicado para este número de página'
                elif pagina >= 20 and pagina < 200:
                    return pagina * (1 - 0.15)
                elif pagina >= 200 and pagina < 2000:
                    return pagina * (1 - 0.20)
                elif pagina >= 2000 and pagina < 20000: 
                    return pagina * (1 - 0.25)
        except ValueError:
            print('Valor inválido. Tente um número inteiro.')


def servico_extra():
    print('Deseja algum serviço extra? \n1 - Encardenação simples - R$15,00 \n2 - Encardenação de capa dura - R$40,00 \n0 - Não deseja mais nada')
    while True:
        extra = input('Selecione algum serviço: ')
        if extra == '0':
            return 0.00
        elif extra == '1':
            return 15.00
        elif extra == '2':
            return 40.00
        else:
            return 'Opção inválida. Tente novamente'

servico = escolha_servico()
pagina = num_pagina()
extra = servico_extra()

total = (servico * pagina) + extra

print(f'Valor total: R${total:.2f}')



