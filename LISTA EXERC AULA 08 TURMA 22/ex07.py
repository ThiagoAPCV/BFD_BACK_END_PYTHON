'''7. Problema - Ficha de Cadastro
Crie um arquivo .py. Dentro do seu arquivo, construa um código que define
uma função cadastrar_usuario que aceite nome e email como argumentos
obrigatórios e qualquer outra informação como kwargs. Imprima todos os
dados recebidos.
Exemplo de uso: cadastrar_usuario(nome="Ana", email="ana@email.com",
idade=30, cidade="Salvador")'''

def cadastrar_usuario(nome, email, **kwargs):
    print('Nome', nome)
    print('E-mail: ',email)
    for chave, valor in kwargs.items(): # Percorre os argumentos extras (kwargs)
        print(f"{chave.capitalize()}: {valor}")

cadastrar_usuario(nome="Thiago", email="thiagoo@email.com", idade=44, cidade="Recife")

