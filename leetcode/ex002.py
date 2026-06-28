nums = [100, 4, 200, 1, 3, 2]

num_set = set(nums)
maior_seq = 0

for num in nums:
    if num -1 not in num_set:
        num_atual = num
        maior_seq = 1

        while num_atual +1 in num_set:
            num_atual += 1
            maior_seq += 1
        maior_seq = max(maior_seq, num_atual)

print(maior_seq)

        
    



