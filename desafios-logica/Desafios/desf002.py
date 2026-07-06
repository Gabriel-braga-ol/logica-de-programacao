while True:
    nome = input('Digite seu nome: ')
    senha = input('Digite sua senha: ')
    if senha.lower() == nome.lower():
        print('A senha não pode ser igual ao nome do usuário.')
        continue
    break