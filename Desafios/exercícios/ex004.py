print('Bem vindo(a) a biblioteca do Gabriel Braga')

lista_livros = []

id_global = 12345678
print('-'*20, 'Menu cadastrar livro', '-'*20)

def cadastrar_livro(id):
    nome = str(input('Digite o nome do livro: '))
    autor = str(input('Digite o nome do autor: '))
    editora = str(input('Digite o nome da editora: '))

    livro = {
        'id': id,
        'nome': nome,
        'autor': autor,
        'editora': editora
    }

    lista_livros.append(livro.copy())
    print(f'Livro {nome} cadastrado com sucesso')

def consultar_livros():
    while True:
        print('Selecione a opção desejada: \n1. Consultar todos \n2. Consultar por id \n3. Consultar por autor \n4. Retornar ao menu')
        consulta = int(input('Digite uma opção: '))
        if consulta not in [1, 2, 3, 4]:
            print('Opcão inválida. Tente novamente')
            continue
        else:
            if consulta == 1:
                print('\nLivros cadastrados:')
                if not lista_livros:
                    print('Nenhum livro cadastrado.')
                else:
                    for livro in lista_livros:
                        print(f'ID: {livro['id']} | Nome: {livro['nome']} | Autor: {livro['autor']} | Editora: Livro: {livro['editora']}')

            elif consulta == 2:
                busca = int(input('Digite o ID do livro: '))
                encontrado = False
                for livro in lista_livros:
                    if livro['id'] == busca:
                        print('\nLivro encontrado.')
                        print(f'ID: {livro['id']} | Nome: {livro['nome']} | Autor: {livro['autor']} | Editora: {livro['editora']}')
                        encontrado = True
                        break
            elif consulta == 3:
                busca_autor = str(input('Digite o nome do autor: ')).lower()
                resultados = [l for l in lista_livros if busca_autor in l['autor'].lower()]
                if resultados:
                    print(f'\nLivros do autor {busca_autor}: ')
                    for livro in resultados:
                        print(f'ID: {livro['id']} | Nome: {livro['nome']} | Autor: {livro['autor']} | Editora: {livro['editora']}')
                else:
                    print('Nenhum livro encontrado para este autor')
            elif consulta == 4:
                return

def remover_livro():
    while True:
        remover_id = int(input('Digite o ID que será removido: '))
        for livro in lista_livros:
            if livro['id'] == remover_id:
                lista_livros.remove(livro)
                print(f'Livro com ID {remover_id} removido com sucesso')
                return 
        print('ID inválido. Tente novamente.')

while True:
    print('Selecione uma opção: \n1. Cadastar livro \n2. Consultar livro \n3. Remover livro \n4. Encerrar programa')
    usuario = int(input('Escolha uma das opções: '))
    if usuario not in [1, 2, 3, 4]:
        print('Opção inválida. Tente novamente.')
        continue
    else:
        if usuario == 1:
            cadastrar_livro(id_global)
            id_global += 1
        elif usuario == 2:
            consultar_livros()
        elif usuario == 3:
            remover_livro()
        elif usuario == 4:
            print('Encerrando o programa')
            break

