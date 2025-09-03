'''13. Problema - Ranking de Vendas
Crie um arquivo .py. Escreva um código que vai armazenar a sequência
'João', 'Maria', 'Pedro', 'Ana' em uma lista chamada vendedores. Você precisa
imprimir a posição e o valor de cada elemento da lista, faça isso utilizando o
enumerate(), comece a contagem do número 1.
'''

vendedores = ['João', 'Maria', 'Pedro', 'Ana']

print("Relação de Vendedores:")
for posicao, nome in enumerate(vendedores, start=1): #Enumerate => percorre a lista, adicionando uma numeração começando em 1
    print(f"{posicao} - {nome}")