while True:
    try:
        nota = int(input('Digite uma nota entre 0 e 10: '))
        if nota in [0,1,2,3,4,5,6,7,8,9,10]:
            break
        else:
            print('Nota inválida')
    except ValueError:
        print('Digite um número inteiro.')
        # continue