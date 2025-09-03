'''11. Problema - Gerenciamento de Estoque
Crie um arquivo .py. Crie um conjunto chamado frutas que vai armazenar as
seguintes informações 'maçã', 'banana', 'manga', 'laranja'. Agora adicione
uma nova fruta a esse conjunto 'uva', depois remova um dos elementos
existentes 'banana' e 'manga'.
'''

frutas = {'maçã', 'banana', 'manga', 'laranja'}
print("\nConjunto inicial de frutas:")
print(frutas)
frutas.add('uva')
frutas.remove('banana')
frutas.remove('manga')
print("\nConjunto de frutas após alterações:")
print(frutas)