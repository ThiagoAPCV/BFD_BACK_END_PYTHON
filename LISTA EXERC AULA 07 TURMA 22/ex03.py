'''3. Problema - Registro de Vendas
Crie um arquivo .py .Escreva um código que vai armazenar a sequência 1200,
1500, 1100, 2000, 2500, 1800, 1300 de vendas de cada dia da semana em
uma estrutura de dados do tipo lista chamada vendas semana. Pense no
seguinte cenário, você precisa saber o valor total de vendas durante a
semana e além disso, você precisa descobrir qual dia da semana com o
menor valor de venda.'''

vendas_semana = [1200, 1500, 1100, 2000, 2500, 1800, 1300]

print("Vendas da semana:")
print(vendas_semana)

total_vendas = sum(vendas_semana)
print(f"\nValor total de vendas na semana: {total_vendas}")

menor_venda = min(vendas_semana)

dia_menor_venda = vendas_semana.index(menor_venda)

dias = ["Segunda Feira", "Terça Feira", "Quarta Feira", "Quinta Feira", "Sexta Feira", "Sábado", "Domingo"]

print(f"\nO menor valor de venda foi {menor_venda}, ocorrido na {dias[dia_menor_venda]}.")