'''10. Problema - Verificador de Par ou Ímpar
Crie um arquivo .py. Dentro do seu arquivo, construa um código que crie uma
variável e_par que armazene/receber uma função lambda. Esta função
lambda deve verificar se um número qualquer é par e retornar True se o
número for par, e False se for ímpar.
Exemplo de uso: e_par(4) deve retornar True.
'''

e_par = lambda numero: numero % 2 == 0

# Testando a função
print(e_par(4))  # True
print(e_par(7))  # False