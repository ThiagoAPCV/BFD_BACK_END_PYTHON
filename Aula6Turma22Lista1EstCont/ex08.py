cor = input("Digite a cor do semáforo (verde, amarelo ou vermelho): ").strip().lower()

match cor:
    case "verde":
        print("Siga em frente.")
    case "amarelo":
        print("Atenção! Prepare-se para parar.")
    case "vermelho":
        print("Pare o veículo.")
    case _:
        print("Sinal inválido. Por favor, digite verde, amarelo ou vermelho.")
