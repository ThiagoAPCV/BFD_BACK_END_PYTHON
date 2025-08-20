dividendo = int(input("Digite o dividendo: "))
divisor = int(input("Digite o divisor: "))

# Evitar divisão por zero
if divisor != 0:
    resultado = dividendo / divisor   # divisão normal
    RESTO = dividendo % divisor       # resto da divisão
    print(f"{dividendo} / {divisor} = {resultado} | resto = {RESTO}")
else:
    print("Erro: divisão por zero não é permitida.")