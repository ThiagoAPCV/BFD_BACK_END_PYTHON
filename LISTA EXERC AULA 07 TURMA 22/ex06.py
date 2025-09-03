'''6. Problema - Identificação de Arquivos
Crie um arquivo .py. Escreva um código que vai armazenar os seguintes
dados de uma sequência de arquivos 'documento.pdf', 'foto.jpg',
'relatorio.pdf', 'planilha.xlsx' em uma tupla chamada arquivos. Você precisa
contar quantas vezes a extensão .pdf aparece dentro da tupla e mostra o
resultado na tela para os usuários.
'''

arquivos = ('documento.pdf', 'foto.jpg', 'relatorio.pdf', 'planilha.xlsx')

qnt_pdf = sum(1 for arquivo in arquivos if arquivo.endswith('.pdf'))

print("\nArquivos:", arquivos)
print(f"A quantidade de arquivos do tipo PDF são: {qnt_pdf}\n")