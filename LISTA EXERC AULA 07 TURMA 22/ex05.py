'''5. Problema - Análise de Dados de Vendas
Crie um arquivo .py. Escreva um código que vai armazenar os seguintes
dados de uma venda de produto e a quantidade dele 'Caderno', 15 em uma
tupla chamada venda. Você precisa calcular o valor total da venda, nesse
caso imagine que o preço unitário do produto é R$ 25,00. Mostre o resultado
na tela para o usuário.'''

venda = ('Caderno', 15)
ítem, qnt = venda
preço_unitario = 25.00

total_venda = preço_unitario * qnt

print("\nProduto:", ítem)
print("Quantidade vendida:", qnt)
print("Preço unitário: R$", preço_unitario)
print(f'\nO valor total de vendas do {ítem} foi de R${total_venda}.\n')