num1 = int(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))

POTENCIA = num1 ** num2
DIVISAO_INTEIRA = num1 // num2 if num2 != 0 else "Erro: divisão por zero"

print(f"{num1} ** {num2} = {POTENCIA}")
print(f"{num1} // {num2} = {DIVISAO_INTEIRA}")