"""
Maximum subarray problem

Encontre o subarrays contiguo de maior valor

Array

[5, 6, -15, 2, 4, -1, 12, -8]

Subarrays

[5] sum = 5
[5, 6] sum = 11
[6, -15, 2] sum = -7
[2, 4, -1, 12] sum = -17

"""

"""
x = [5, 6, -15, 2, 4, -1, 12, -8]

min_value = float('-inf')
for i in range(len(x)):
    for j in range (i, len(x)):
        soma = 0
        for k in range(i, j + 1):
            soma += x[k]
        
        if soma > min_value:
            min_value = soma

print(min_value)  

Método menos eficiente + lento
complexiade de O(n**3)
"""

x = [5, 6, -15, 2, 4, -1, 12, -8]  

max_soma = x[0]
soma_atual = x[0]

for i in range(1, len(x)):
    if soma_atual + x[i] > x[i]:
        soma_atual += x[i]
    else:
        soma_atual = x[i]

    if soma_atual > max_soma:
        max_soma = soma_atual

print(max_soma)