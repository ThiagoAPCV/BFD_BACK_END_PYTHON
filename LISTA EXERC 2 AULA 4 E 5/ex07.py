idade_motorista = int(input("Qual a sua idade? "))

# Corrigindo a conversão de string para boolean
tem_carteira_input = input("Você tem carteira de motorista? (True/False) ")
tem_carteira = tem_carteira_input.strip().lower() == "true"

pode_dirigir = idade_motorista >= 18 and tem_carteira  # use "and" para exigir as duas condições

print(f"Pode dirigir? {pode_dirigir}")