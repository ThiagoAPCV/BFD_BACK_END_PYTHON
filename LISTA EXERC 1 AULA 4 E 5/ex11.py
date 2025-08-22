# Programa para verificar se o usuário é maior ou menor de idade

IDADE_MINIMA = 18

idade_usuario = int(input("Digite a sua idade: "))

maior_de_idade = idade_usuario >= IDADE_MINIMA
menor_de_idade = idade_usuario < IDADE_MINIMA

print(f"O usuário é maior de idade? {maior_de_idade}")
print(f"O usuário é menor de idade? {menor_de_idade}")