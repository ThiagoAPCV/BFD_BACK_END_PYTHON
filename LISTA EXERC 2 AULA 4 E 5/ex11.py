# Programa para calcular o preço de um carro alugado

km_percorridos = float(input("Digite a quantidade de Km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias que o carro foi alugado: "))

preco_por_dia = 60.0
preco_por_km = 0.15

preco_total = (dias_alugados * preco_por_dia) + (km_percorridos * preco_por_km)

print(f"O preço total a pagar é: R$ {preco_total:.2f}")