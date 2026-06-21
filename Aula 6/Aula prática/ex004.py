cadastro = {
    'Nome:': [],
    'Sexo:': [],
    'Ano de nascimento:': []
}

total = 0

while True:
    usuario = input('Deseja cadastrar uma pessoa: ').upper()
    if usuario == 'N':
        break
    if usuario not in ['N', 'S']:
        print('Digite apenas S ou N')
        continue
    else:
        nome = input('Digite o nome a pessoa: ')
        sexo = input('Digite o sexo da pessoa: ').upper()
        ano_nasc = input('Digite o ano de nascimento da pessoa: ')

    
    cadastro['Nome:'].append(nome)
    cadastro['Sexo:'].append(sexo)
    cadastro['Ano de nascimento:'].append(ano_nasc)

    print(cadastro)
