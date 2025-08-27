'''Crie um arquivo .py. Escreva um código que vai armazenar a sequência 
'Bruno', 'Ana', 'Carlos', 'Denise', 'Felipe' de alunos em uma estrutura 
de dados do tipo lista chamada alunos. Pense no seguinte cenário, você 
precisa modificar essa lista, mostrando os nomes dos alunos em ordem 
decrescente e você deve acessar a posição dos alunos(as) Felipe e Ana e 
mostrar na tela o nome desses alunos. 
'''
alunos = ['Bruno', 'Ana', 'Carlos', 'Denise', 'Felipe']
alunos.sort(reverse=True)
print("Lista de alunos em ordem decrescente:", alunos)

indice_felipe = alunos.index('Felipe')
indice_ana = alunos.index('Ana')

print(f"Aluno na posição {indice_felipe}: {alunos[indice_felipe]}")
print(f"Aluno na posição {indice_ana}: {alunos[indice_ana]}")
