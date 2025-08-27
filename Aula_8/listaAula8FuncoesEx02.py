'''Crie um arquivo .py. Dentro do seu arquivo, construa um código que define uma 
função que receba um texto qualquer como argumento. A função deve retornar o 
valor informado porém com a ordem inversa e esse valor deve ser mostrado na tela.
'''

def inverter_texto(texto):
    return texto[::-1]

entrada = input("Digite um nome qualquer: ")
texto_invertido = inverter_texto(entrada)
print("Texto invertido:", texto_invertido)