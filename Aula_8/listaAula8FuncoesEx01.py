'''Crie um arquivo .py. Dentro do seu arquivo, construa um código que define uma
 função que receba um nome como argumento. A função deve retornar uma mensagem 
 de saudação personalizada, por exemplo: "Olá, [nome]! Bem-vindo(a)!".
'''
def saudacao(nome):
    return f"Olá, {nome}! Bem-vindo(a)!"

nome_usuario = input("Digite seu nome: ")
mensagem = saudacao(nome_usuario)
print(mensagem)