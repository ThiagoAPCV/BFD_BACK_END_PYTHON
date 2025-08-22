# Programa para calcular potência e divisão inteira

num1 = int(input("Digite um valor inteiro: "))
num2 = int(input("Digite outro valor inteiro: "))

POTENCIA = num1 ** num2          # num1 elevado a num2
DIVISAO_INTEIRA = num1 // num2   # divisão inteira de num1 por num2

print(f"{num1} ** {num2} = {POTENCIA}")
print(f"{num1} // {num2} = {DIVISAO_INTEIRA}")