"""
Two sum problem
"""
nums = [11, 15, 2, 7]
alvo = 9
dic = {}

for i, j in enumerate(nums):
    complement = alvo - j 
    if complement in dic:
        resultado = [dic[complement], i]
        break
    dic[j] = i

print(resultado)
