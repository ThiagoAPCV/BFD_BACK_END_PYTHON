IDADE_MINIMA = 18
idade_usuario = int(input("Digite sua idade: "))

if idade_usuario >= IDADE_MINIMA:
    print("O usuário é maior de idade.")
elif idade_usuario == 16 or idade_usuario == 17:
    print("O usuário é menor e tem 16 ou 17 anos.")
else:
    print("O usuário é menor de idade.")
