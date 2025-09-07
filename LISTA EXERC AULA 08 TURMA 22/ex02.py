'''2. Problema - Inversor de string
Crie um arquivo .py. Dentro do seu arquivo, construa um código que define
uma função que receba um texto qualquer como argumento. A função deve
retornar o valor informado porém com a ordem inversa e esse valor deve ser
mostrado na tela.
'''

def inverterTexto (texto):
    return texto[::-1]

texto = 'Um texto qualquer como argumento'
print(f'Texto original: {texto}')
print(f'Texto invertido: {inverterTexto(texto)}')
