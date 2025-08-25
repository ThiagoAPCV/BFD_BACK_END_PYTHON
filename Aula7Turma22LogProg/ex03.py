vendas_semana = [1200, 1500, 1100, 2000, 2500, 1800, 1300]

dias_semana = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"]

total_vendas = sum(vendas_semana)

menor_venda = min(vendas_semana)
indice_menor = vendas_semana.index(menor_venda)
dia_menor_venda = dias_semana[indice_menor]

print(f"Total de vendas da semana: R$ {total_vendas}")
print(f"Menor valor de venda foi R$ {menor_venda} na {dia_menor_venda}.")
