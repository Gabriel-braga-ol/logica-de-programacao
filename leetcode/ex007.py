"""Find the longest common prefix"""

strs = ["flower","flow","flight"]

def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # Pega a primeira string como candidato inicial de prefixo
    prefixo = strs[0]
    
    # Compara o candidato com cada uma das outras strings
    for palavra in strs[1:]:
        # Enquanto a palavra não começar com o prefixo atual, vai cortando o final do prefixo
        while not palavra.startswith(prefixo):
            prefixo = prefixo[:-1]  # remove o último caractere
            if prefixo == "":
                return ""
    
    return prefixo
        
print(longest_common_prefix((["flower","flow","flight"])))
print(longest_common_prefix((["monday","sun","dog"])))
    
   

        