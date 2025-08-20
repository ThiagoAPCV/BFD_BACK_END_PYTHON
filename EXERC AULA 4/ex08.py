saldo_bancario = 1000.0

# Entrada de dados do usuário
deposito = float(input("Digite o valor do depósito: "))
saque = float(input("Digite o valor do saque: "))
juros = float(input("Digite o fator de juros: "))

# Operações com operadores de atribuição
saldo_bancario += deposito     # Adiciona o depósito
saldo_bancario -= saque        # Subtrai o saque
saldo_bancario *= juros        # Aplica o fator de juros

print("O saldo bancário final é:", saldo_bancario)