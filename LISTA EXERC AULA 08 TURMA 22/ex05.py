'''5. Problema - Média notas
Crie um arquivo .py. Dentro do seu arquivo, construa um código que define
uma função calcular_media que aceita qualquer quantidade de notas (*args)
e retorne a média delas.
Exemplo de uso: calcular_media(8.5, 9.0, 7.5) deve retornar 8.33.'''


def calcular_media(*args):
    if len(args) == 0:  # Evita divisão por zero
        return 0
    return round(sum(args) / len(args), 2) #round para 2 casas decimais

print(calcular_media(2, 5.1, 5.2, 8.2)) #média = 5.12
print(calcular_media()) #retornará zero como defnido na função.
