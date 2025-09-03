'''2. Problema - Cadastro de Alunos
Crie um arquivo .py. Escreva um código que vai armazenar a sequência
'Bruno', 'Ana', 'Carlos', 'Denise', 'Felipe' de alunos em uma estrutura de dados
do tipo lista chamada alunos. Pense no seguinte cenário, você precisa
modificar essa lista, mostrando os nomes dos alunos em ordem decrescente
e você deve acessar a posição dos alunos(as) Felipe e Ana e mostrar na tela
o nome desses alunos.'''

alunos = ['Bruno', 'Ana', 'Carlos', 'Denise', 'Felipe']

print("Lista original:")
print(alunos)

alunos.sort(reverse=True)

print("\nLista em ordem decrescente:")
print(alunos)


pos1 = alunos.index('Felipe')
pos2 = alunos.index('Ana')

print(f"\nO aluno {alunos[pos1]} está na posição {pos1} da lista.")
print(f"A aluna {alunos[pos2]} está na posição {pos2} da lista.\n")