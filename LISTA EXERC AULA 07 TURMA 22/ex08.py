'''8. Problema - Ficha Médica
Crie um arquivo .py. Escreva um código que vai armazenar os seguintes
dados de um paciente 'nome': 'João', 'idade': 35, 'peso': 80, 'altura': 1.75 em
um dicionário chamado paciente. O paciente passou a altura errada e agora
você tem que alterar o valor da altura para 1.80, faça isso e mostre na tela.
'''
paciente = {'nome': 'João', 'idade': 35, 'peso': 80, 'altura': 1.75}

print("Dados iniciais do paciente:")
print(paciente)

paciente['altura'] = 1.80

print("\nDados do paciente após correção da altura:")
print(paciente)