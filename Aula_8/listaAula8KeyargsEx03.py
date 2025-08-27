def contar_vogais(texto):
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador


entrada = input("Digite um texto: ")
quantidade = contar_vogais(entrada)
print(f"Quantidade de vogais no texto: {quantidade}")