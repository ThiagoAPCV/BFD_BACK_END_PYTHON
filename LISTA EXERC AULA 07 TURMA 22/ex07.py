'''7. Problema - Catálogo de Produtos
Crie um arquivo .py. Escreva um código que vai armazenar os seguintes
dados de produto Crie 'nome': 'Mouse Gamer', 'preço': 150.00, 'estoque': 50 em
um dicionário chamado de catalogo. Agora você deve adicionar um novo
produto dentro do dicionário catalogo, esse produto contém os seguintes
dados 'nome': 'Teclado Mecânico', 'preço': 450.00, 'estoque': 30. Após isso,
mostre os todos os valores e chaves do dicionário.
'''
catalogo = {1: {'nome': 'Mouse Gamer', 'preço': 150.00, 'estoque': 50}}

catalogo[2] = {'nome': 'Teclado Mecânico', 'preço': 450.00, 'estoque': 30}

print("Catálogo de Produtos:\n")
for chave, valor in catalogo.items():  # chave do catálogo
    print(f"Produto {chave}:")
    for dado, info in valor.items():  # percorrendo o dicionário interno de cada chave catálogo 
        print(f"  {dado}: {info}")
    print()

