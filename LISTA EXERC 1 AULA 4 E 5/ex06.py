# Programa para calcular potência usando operador de atribuição (**=)

numero = 2

expoente = int(input("Digite o valor do expoente (inteiro): "))

# Guardando o valor inicial para exibir depois
numero_inicial = numero

numero **= expoente

print(f"Valor inicial de numero: {numero_inicial}")
print(f"Valor final de numero (após elevar à potência): {numero}")