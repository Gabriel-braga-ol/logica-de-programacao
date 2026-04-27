"""
Funções - bloco de código que exerce uma determinada tarefa
podem receber valores para parâmetros (argumentos)
e retornar um valor específico
por padrão, funções em python retornam none (nada)

argumento nomeado - tem nome com sinal de igual
argumento não nomeado - recebe apenas o argumento (valor)

ao definir uma função, os parâmetros podem
ter valores padrão. Casso o valor não seja
enviado para o parâmetro, o valor padrão será usado
refatorar: editar o seu código.

Escopo de funções em python
Escopo pode ser global ou local
global - onde todo código é alcançável
local - onde apenas nomes do mesmo local podem ser alcançados

Return - retorno de valores das funções

args - argumentos não nomeados
*args (empacotamento e desempacotamento)
"""

# def imprimir(a, b, c):
#     print(a, b, c)
    

# imprimir(1,2,3)
# imprimir(4,5,6)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}')

saudacao('Gabriel')
saudacao('Maria')
saudacao('Helena')
saudacao() # Se o valor não for passado, a função usará o valor atribuído na variável nome, neste caso, 'Sem nome'