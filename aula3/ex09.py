# Solicita ao usuário o nome do produto e armazena na variável nome_produto
nome_produto = input("Digite o nome do produto: ")

# Solicita ao usuário o preço do produto, converte para float e armazena em preco_produto
preco_produto = float(input("Digite o preço do produto: "))

# Exibe o nome e preço do produto usando f-string
# :.2f formata o número para ter 2 casas decimais
print(f"O produto {nome_produto} custa R$ {preco_produto:.2f}.")