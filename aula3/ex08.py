# Importa o módulo datetime para trabalhar com data e hora
import datetime

# Captura a data e hora atuais
hora_atual = datetime.datetime.now()

# Solicita ao usuário o seu nome e armazena na variável nome_usuario
nome_usuario = input("Digite o seu nome: ")

# Exibe a saudação personalizada com a hora atual formatada
# strftime('%H:%M') formata para mostrar horas e minutos no formato 24h
print(f"Olá, {nome_usuario}! Agora são {hora_atual.strftime('%H:%M')} horas.")