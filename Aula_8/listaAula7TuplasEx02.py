'''Crie um arquivo .py. Escreva um código que vai armazenar os seguintes dados 
de uma venda de produto e a quantidade dele  'Caderno', 15 em uma tupla chamada 
venda. Você precisa calcular o valor total da venda, nesse caso imagine que o 
preço unitário do produto é R$ 25,00. Mostre o resultado na tela para o usuário. 
'''

venda = ('Caderno', 15)

preco_unitario = 25.00

# Calculando o valor total da venda
produto, quantidade = venda
valor_total = quantidade * preco_unitario

print(f"Produto: {produto}")
print(f"Quantidade vendida: {quantidade}")
print(f"Preço unitário: R${preco_unitario:.2f}")
print(f"Valor total da venda: R${valor_total:.2f}")