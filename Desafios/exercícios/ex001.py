"""
Imagina-se que você é um dos programadores responsáveis pela construção
de um app de vendas para uma determinada empresa X que vende em atacado. Uma das
estratégias de vendas dessa empresa X é dar desconto maior conforme o valor da compra,
conforme a listagem abaixo:os futuros chats."
• Se valor_total for menor que 2500 o desconto será de 0%;
• Se valor_total for maior ou igual que 2500 e menor que 6000 o desconto será de
4%;
• Se valor_total for maior ou igual que 6000 e menor que 10000 o desconto será
de 7%;
• Se valor_total for maior ou igual que 10000 o desconto será de 11%;
"""

nome = 'Gabriel Braga'
print(f'Bem vindo(a) a loja do {nome}!')
valor_produto = float(input('Digite o valor do prodtudo: '))
qtd_produto = int(input('Digite a quantidade: '))
valor_total = valor_produto * qtd_produto

# Aplicando o desconto

if valor_total < 2500:
    print(f'O valor total de R${valor_total} não corresponde aos requisitos da promoção, portanto, não haverá desconto')
elif valor_total >= 2500 and valor_total < 6000:
    desconto = valor_total * (4 / 100)
    preco_final = valor_total - desconto
    print(f'O valor com desconto é R${preco_final:,.2f}')
    print(f'O valor sem desconto é R${valor_total:,.2f}')
elif valor_total >= 6000 and valor_total < 10000:
    desconto_2 = valor_total * (7 / 100)
    preco_final_2 = valor_total - desconto_2
    print(f'O valor com desconto é R${preco_final_2:,.2f}')
    print(f'O valor sem desconto é R${valor_total:,.2f}')
else:
    desconto_3 = valor_total * (11 / 100)
    preco_final_3 = valor_total - desconto_3
    print(f'O valor com desconto é R${preco_final_3:,.2f}')
    print(f'O valor sem desconto é R${valor_total:,.2f}')