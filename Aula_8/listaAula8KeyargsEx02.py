'''Crie um arquivo .py. Dentro do seu arquivo, construa um código que define 
uma função calcular_media que aceite qualquer quantidade de notas (*args) e 
retorne a média delas.
Exemplo de uso: calcular_media(8.5, 9.0, 7.5) deve retornar 8.33.
'''

def calcular_media(*args):
    if len(args) == 0:
        return 0  # Evita divisão por zero
    return round(sum(args) / len(args), 2)

media = calcular_media(2.4, 6.0, 7.5)
print(f"Média: {media}")
