"""
Given a sorted array of distinct integers and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
"""

nums = [1,3,5,6]


def insert(nums, alvo):
    for i, j in enumerate(nums):
        if j >= alvo:
            return i
    return len(nums)

print(insert(nums, 5))
    
   

            

        
        