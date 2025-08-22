# Programa para receber dois números e calcular operações aritméticas

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))

soma = A + B
subtracao = A - B
multiplicacao = A * B
divisao = A / B  # divisão normal
divisao_inteira = A // B  # divisão inteira
resto = A % B    # resto da divisão
potencia = A ** B  # A elevado a B

print(f"{A} + {B} = {soma}")
print(f"{A} - {B} = {subtracao}")
print(f"{A} * {B} = {multiplicacao}")
print(f"{A} / {B} = {divisao}")
print(f"{A} // {B} = {divisao_inteira}")
print(f"{A} % {B} = {resto}")
print(f"{A} ** {B} = {potencia}")