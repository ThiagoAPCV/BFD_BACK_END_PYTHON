# Programa para calcular o salário mensal do usuário

valor_hora = float(input("Digite quanto você ganha por hora: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))

salario_mensal = valor_hora * horas_trabalhadas

print(f"O salário total no mês é: R$ {salario_mensal:.2f}")