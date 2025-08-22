# Programa para atualizar o estoque com base em um valor informado pelo usuário

estoque = 50

valor = int(input("Digite a quantidade a adicionar ao estoque: "))

estoque_inicial = 50
estoque += valor

print(f"Estoque inicial: {estoque_inicial}")
print(f"Estoque final: {estoque}")