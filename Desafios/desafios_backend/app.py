"""
Dado um array de números inteiros nums, retorne true se algum valor aparece mais de uma vez, caso contrário, retorne false

input: nums = [1,2,2,3]

output: True

input: nums = [1,2,3,4]

output: False
"""

"""
def duplicado(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False
            

lista = [1, 2, 2, 3]
print(duplicado(lista))

Método de maior complexidade O(n**2)
"""

def duplicado(nums):
    conj = []
    for i in nums:
        if i in conj:
            return True
        conj.append(i)
    return False
        
lista = [1, 2, 4, 3, 3]
print(duplicado(lista))

