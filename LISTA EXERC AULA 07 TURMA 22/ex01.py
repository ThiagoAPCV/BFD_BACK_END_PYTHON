'''1. Problema - Gerenciamento de Estoque
Crie um arquivo .py. Escreva um código que vai armazenar a sequência
'camiseta', 'calça', 'meia', 'jaqueta' de produtos em uma estrutura de dados
do tipo lista chamada Estoque. Pense no seguinte cenário, acaba de chegar
um novo estoque de um novo produto 'boné' adicione esse novo produto à
lista e remova o produto 'calça' que não tem estoque disponível.
'''

estoque = ['camiseta', 'calça', 'meia', 'jaqueta']

print("Estoque inicial:")
print(estoque)

estoque.append('boné')

estoque.remove('calça')

print("\nEstoque após substituições:")
print(estoque)