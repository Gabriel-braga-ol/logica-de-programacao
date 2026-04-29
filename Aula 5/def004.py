"""
Escopo de funções em python.
Escopo pode ser global ou local.
global - onde todo código é alcançável.
local - onde apenas nomes do mesmo local podem ser alcançados.
não temos acesso a nomes de escopos internos nos escops externos.
a palavra global faz uma variável do escopo externo ser a mesma do escopo interno.
"""

x = 1

def escopo():
    # global x    
    x = 10
    def outra_funcao():
        # global x    
        x = 11
        y = 2
        print(x, y)
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)