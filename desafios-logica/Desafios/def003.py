while True:
    nome = input('Nome: ')
    idade = int(input('idade: '))
    salario = float(input('Salário: '))
    sexo = input('Sexo (M/F): ').upper()
    estado_civil = input('Estado civil (s, c, v, d): ').upper()

    if len(nome) <= 3 or (idade < 0 or idade > 150) or salario <= 0 or sexo not in ['F', 'M'] or estado_civil not in ['S', 'C', 'V', 'D']:
        print('Dados inválidos. Digite novamente')
        continue
    break
    
    
        

    
    