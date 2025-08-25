"""Crie um arquivo .py. Defina uma lista de números inteiros: numeros = [10, 20, 30, 40, 50].
Use um laço for para calcular a soma de todos os elementos dessa lista e exiba o resultado
na tela."""

numeros = [10, 20, 30, 40, 50]

soma = 0

for num in numeros:
    soma += num

print(f"A soma dos elementos da lista é: {soma}")
