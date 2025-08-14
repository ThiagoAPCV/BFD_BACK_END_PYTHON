import datetime

# Corrigido: nome de variável sem espaço
hora_atual = datetime.datetime.now()

# Corrigido: nome de variável válido e string entre aspas
nome_usuario = input("Digite o seu nome: ")

# Corrigido: uso correto da f-string
print(f"Olá, {nome_usuario}! Agora são {hora_atual.strftime('%H:%M')} horas.")