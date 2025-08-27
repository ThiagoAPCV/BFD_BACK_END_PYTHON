'''Crie um arquivo .py. Dentro do seu arquivo, construa um código que define 
uma função que receba um texto qualquer como argumento. A função deve retornar
 a quantidade de vogais (a, e, i, o, u) do valor informado e esse resultado deve
   ser mostrado na tela.
'''

def contar_vogais(texto):
    vogais = 'aeiouAEIOU'
    contador = 0
    for char in texto:
        if char in vogais:
            contador += 1
    return contador

entrada = input("Digite um texto qualquer: ")
quantidade = contar_vogais(entrada)
print(f"Quantidade de vogais no texto: {quantidade}")