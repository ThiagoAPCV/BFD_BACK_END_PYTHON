'''Crie um arquivo .py. Escreva um código que vai armazenar os seguintes dados
 de produto Crie 'nome': 'Mouse Gamer', 'preço': 150.00, 'estoque': 50 em um 
 dicionário chamado de catalogo. Agora você deve adicionar um novo produto
   dentro do dicionário catalogo, esse produto contém os seguintes dados
     'nome': 'Teclado Mecânico', 'preço': 450.00, 'estoque': 30. Após isso,
       mostre os todos os valores e chaves do dicionário.
'''

catalogo = {
    'produto1': {
        'nome': 'Mouse Gamer',
        'preço': 150.00,
        'estoque': 50
    }
}

# Adicionando um novo produto ao catálogo
catalogo['produto2'] = {
    'nome': 'Teclado Mecânico',
    'preço': 450.00,
    'estoque': 30
}

print("Catálogo de Produtos:")
for chave, valor in catalogo.items():
    print(f"\n{chave}:")
    for sub_chave, sub_valor in valor.items():
        print(f"  {sub_chave}: {sub_valor}")