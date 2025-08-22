# Programa para dividir tarefas igualmente entre pessoas

tarefas = 20

numero_pessoas = int(input("Digite o número de pessoas: "))

tarefas_inicial = tarefas

tarefas //= numero_pessoas

print(f"Total de tarefas inicial: {tarefas_inicial}")
print(f"Cada pessoa receberá: {tarefas} tarefas")