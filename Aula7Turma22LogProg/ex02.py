alunos = ["Bruno", "Ana", "Carlos", "Denise", "Felipe"]

# Ordem decrescente
alunos.sort(reverse=True)

# Lista ordenada
print("Lista de alunos em ordem decrescente:")
print(alunos)

indice_felipe = alunos.index("Felipe")
indice_ana = alunos.index("Ana")

print(f"Aluno na posição {indice_felipe}: {alunos[indice_felipe]}")
print(f"Aluno na posição {indice_ana}: {alunos[indice_ana]}")
