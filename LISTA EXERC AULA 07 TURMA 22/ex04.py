'''4. Problema - Ficha de Funcionário
Crie um arquivo .py. Escreva um código que vai armazenar os seguintes
dados de um funcionário 'Ana Souza', 'Gerente', 8500.00 em uma tupla
chamada funcionario, a tupla deve conter cada um dos dados do
funcionário. Você precisa pegar cada um desses dados da tupla e
armazená-los em três variáveis, após isso você deve imprimir cada um
desses valores.
'''

funcionario = ('Ana Souza', 'Gerente', 8500.00)
# Desempacotando a tupla em variáveis separadas
nome, cargo, salario = funcionario

print("Dados do funcionário:")
print("Nome:", nome)
print("Cargo:", cargo)
print("Salário:", salario)