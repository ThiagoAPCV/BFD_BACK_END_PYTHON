'''Crie um arquivo .py e defina um dicionário chamado meus_dados para armazenar 
dados pessoais de um usuário, contendo as chaves e valores 
'nome': 'Alice', 'idade': 35 e 'cidade': 'Nova York'. Em seguida, adicione ao 
dicionário um novo par chave-valor 'profissao': 'Médica', modifique o valor da 
chave 'idade' para 40, acesse e imprima o valor associado à chave 'cidade' e,
 por fim, exiba o dicionário completo após todas as operações.'''

meus_dados = {
    'Nome': 'Alice',
    'Idade': 35,
    'Cidade': 'Nova York'
}

# Adicionando um novo par chave-valor
meus_dados['Profissão'] = 'Médica'

# Modificando o valor da chave 'idade'
meus_dados['Idade'] = 40

print("Cidade:", meus_dados['Cidade'])

print("\nDicionário completo:")
for chave, valor in meus_dados.items():
    print(f"{chave}: {valor}")
