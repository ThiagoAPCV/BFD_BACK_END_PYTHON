nota = int(input("Digite uma nota de 1 a 5: "))

match nota:
    case 1:
        print("Muito ruim. Você precisa se esforçar mais.")
    case 2:
        print("Ruim. Ainda está abaixo do esperado.")
    case 3:
        print("Regular. Dá para melhorar!")
    case 4:
        print("Bom. Você está indo bem.")
    case 5:
        print("Excelente! Parabéns pelo desempenho.")
    case _:
        print("Erro: Nota inválida. Digite um valor entre 1 e 5.")
