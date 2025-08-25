"""Crie um arquivo .py. Defina uma lista de números inteiros: numeros = [10, 20, 30, 40, 50].
Use um laço while para calcular a soma de todos os elementos dessa lista e exiba o
resultado na tela.
Obs: Lembre-se de usar uma variável temporária para controlar as quantidades que o bloco
de código vai ser repetido, evitando o loop infinito.
variavel_temporaria = 0
while variavel_temporaria <= 5:
# Os códigos de dentro do while, vão se repetir enquanto a variável temporária
# for menor ou igual a 5, quando a variavel temporaria chegar tiver o valor igual a
# 5 ou maior que 5 os código de dentro do while não vão ser mais repetidos"""

numeros = [10, 20, 30, 40, 50]

soma = 0
variavel_temporaria = 0

while variavel_temporaria < len(numeros):
    soma += numeros[variavel_temporaria]
    variavel_temporaria += 1

print(f"A soma dos elementos da lista é: {soma}")
