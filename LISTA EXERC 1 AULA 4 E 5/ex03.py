# Programa para calcular o resto da divisão de dois números inteiros

dividendo = int(input("Digite o dividendo (valor inteiro): "))
divisor = int(input("Digite o divisor (valor inteiro): "))

quociente = dividendo // divisor   # divisão inteira
RESTO = dividendo % divisor        # resto da divisão

print(f"{dividendo} / {divisor} = {quociente} | resto = {RESTO}")