import random

# contador = 1
# valores_dentro = 0
# valores_fora = 0

# while contador <= 10:
#     x = int(input('Digite um número: '))
#     contador += 1

#     if x >= 10 and x <= 20 :
#         valores_dentro += 1
#         print(x)
#     else:
#         valores_fora += 1

# print(valores_dentro)
# print(valores_fora)
    
valores = random.sample(range(1, 21), 10)

cont = 0
fora = 0
valores_fora = 0
for i in valores:
    if i >= 10 and i <= 20:
        cont += 1
        print(i, end=' ')
    else:
        fora += 1
        valores_fora += i
        

print(f'\nExistem {cont} valores entre 10 e 20')
# print(f'\nExistem {fora} valores que não estão entre 10 e 20')
print(valores)





    
