'''4. Problema - Concatenador de strings
Crie um arquivo .py. Dentro do seu arquivo, construa um código que define
uma função que receba um número variável de strings (*args). A função deve
concatená-las, mesclá-las em um único valor de texto string e retorná-la.
Exemplo de uso: juntar_strings("Olá", " ", "mundo", "!") deve retornar "Olá
mundo!".
'''

def juntar_strings(*args):   # Função para concatenar múltiplas strings. *args permite que a função receba quantos argumentos de string forem necessários.
    return "".join(args)  # Une todas as strings passadas como argumento

texto = juntar_strings("Olá", " ", "mundo", "!")
print(texto)