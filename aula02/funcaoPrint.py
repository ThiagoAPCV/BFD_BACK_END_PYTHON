nome = 'Maria'
idade = 30
print('Olá Mundo!')
print('Seu nome é:', nome)
print('Você tem: ', idade,' anos.')

num1 = 10
num2 = 20
soma = num1 + num2
print('O resultado da soma é: ',soma)
# Saída esperada: O resultado da soma é: 30

dobro = num1 * 2
triplo = num1 * 3
print ('O dobro do numero 1 é: ',dobro,' e o triplo é: ', triplo)
print ('O dobro do numero 1 é: {}, o triplo é: {}'.format(dobro, triplo))

print('O tipo da variável num1 é: ',type(num1))
print('O tipo da variável dobro é: ',type(dobro))
num3 = input('Digite um número: ')
print('O tipo da variável num3 é: ',type(num3))
quadruplo = num3 * 4
print(quadruplo)
print('O tipo da variável quadruplo é: ',type(quadruplo))
num3 = int(num3)
quadruplo = num3 * 4
print(quadruplo)
print('O tipo da variável quadruplo é: ',type(quadruplo))

nome_usuário = input('Qual o seu nome?')
print('Prazer em te conhecer, ', nome_usuário)
#SAída esperada: Prazer em te conhecer, Bruno

email_usuario = input('Digite seu e-mail: ')
print(email_usuario)
#Saída esperadda: (E_mail digitado)