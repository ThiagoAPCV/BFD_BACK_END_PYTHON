'''9. Problema - Busca de livro
Crie um arquivo .py. Dentro do seu arquivo, construa um código que define
uma função chamada buscar_livro que aceite um título obrigatório e kwargs
como filtros de busca (por exemplo, autor="Machado de Assis", ano=1899).
Imprima o título e todos os filtros aplicados'''


def buscar_livro(titulo, **kwargs): 
    print(f'Título: {titulo}')
    
    # Verifica se existem filtros de busca
    if kwargs:
        print('Filtros aplicados:')
        for chave, valor in kwargs.items():
            print(f' - {chave.capitalize()}: {valor}')
    else:
        print('Nenhum filtro aplicado.')

# Ex
buscar_livro('Tecnologia', autor='Thiago', ano=2025)