NOTA_MINIMA = 7.0

nota_final = float(input("Digite sua nota final: "))

if nota_final >= NOTA_MINIMA:
    print("Aprovado!")
elif 5.0 <= nota_final < NOTA_MINIMA:
    print("Você não foi muito bem. Mas ainda consegue recuperar.")
else:
    print("Reprovado!")
