'''Crie um arquivo .py. Escreva um código que vai armazenar os seguintes dados 
de uma sequência de arquivos 'documento.pdf', 'foto.jpg', 'relatorio.pdf', 
'planilha.xlsx' em uma tupla chamada arquivos. Você precisa contar quantas vezes 
a extensão .pdf aparece dentro da tupla e mostra o resultado na tela para os 
usuários.'''

arquivos = ('documento.pdf', 'foto.jpg', 'relatorio.pdf', 'planilha.xlsx')

# Contando quantos arquivos têm a extensão .pdf endswith('TIPO_DO_ARQUIVO')
quantidade_pdf = sum(1 for arquivo in arquivos if arquivo.endswith('.pdf'))

# Exibindo o resultado
print(f"Quantidade de arquivos com extensão .pdf: {quantidade_pdf}")