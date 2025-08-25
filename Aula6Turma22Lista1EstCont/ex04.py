num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))

operador = input("Digite o operador (+, -, *, /, //, %): ")

if operador == "+":
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operador == "-":
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif operador == "*":
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
elif operador == "//":
    if num2 != 0:
        resultado = num1 // num2
        print(f"Resultado: {num1} // {num2} = {resultado}")
    else:
        print("Erro: Divisão inteira por zero não é permitida.")
elif operador == "%":
    if num2 != 0:
        resultado = num1 % num2
        print(f"Resultado: {num1} % {num2} = {resultado}")
    else:
        print("Erro: Módulo por zero não é permitido.")
else:
    print("Operador inválido. Use apenas: +, -, *, /, //, %.")
