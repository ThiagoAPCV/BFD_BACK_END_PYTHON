# Programa para simular operações bancárias com depósito, saque e juros

saldo_bancario = 1000.0

deposito = float(input("Digite o valor do depósito: "))
saque = float(input("Digite o valor do saque: "))
fator_juros = float(input("Digite o fator de juros (exemplo: 1.05 para 5% de aumento): "))

# Guardando saldo inicial para exibir depois
saldo_inicial = saldo_bancario

saldo_bancario += deposito      # adiciona depósito
saldo_bancario -= saque         # subtrai saque
saldo_bancario *= fator_juros   # aplica juros

print(f"Saldo inicial: {saldo_inicial:.2f}")
print(f"Saldo após depósito, saque e aplicação de juros: {saldo_bancario:.2f}")