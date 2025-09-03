'''12. Problema - Registro de Vendas
Crie um arquivo .py . Escreva um código que vai conter uma variável que vai
armazenar alguma frase qualquer. Seu objetivo é contar o número de
palavras únicas na frase fornecida.
Obs: Você pode utilizar os conceitos de lista e conjunto para concluir esse
objetivo. Além disso, você pode utilizar a função split() para dividir uma
string em frases.'''

frase = str(input('Digite uma frase qualquer: '))

palavras = frase.split() # Convertendo a frase em lista de palavras usando split()

palavras_unicas = set(palavras) # Criando um conjunto para eliminar palavras duplicadas

num_palavras_unicas = len(palavras_unicas) # Contando o número de palavras únicas


# Mostrando o resultado
print("Frase:", frase)
print('Lista das palavras contida na frase', palavras)
print("Palavras únicas:", palavras_unicas)
print("Número de palavras únicas:", num_palavras_unicas)