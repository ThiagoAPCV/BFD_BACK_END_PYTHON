'''3. Problema - Contador de vogais
Crie um arquivo .py. Dentro do seu arquivo, construa um código que define
uma função que receba um texto qualquer como argumento. A função deve
retornar a quantidade de vogais (a, e, i, o, u) do valor informado e esse
resultado deve ser mostrado na tela'''

def qntVogais(texto):
    vogais = 'aeiouAEIOU'
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

frase = 'Thiago André.'

print('O texto é: ',frase)
print('A quantidade total de vogais neste texto é de: ', qntVogais(frase))

