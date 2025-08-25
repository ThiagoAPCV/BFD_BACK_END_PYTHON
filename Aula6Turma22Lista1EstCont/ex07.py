status = (
    input(
        "Digite o status atual do pedido (recebido, em_preparação, em_entrega, entregue): "
    )
    .strip()
    .lower()
)

match status:
    case "recebido":
        print("Seu pedido foi recebido e será processado em breve.")
    case "em_preparação":
        print("Seu pedido está em preparação. Em breve será enviado.")
    case "em_entrega":
        print("Seu pedido está a caminho!")
    case "entregue":
        print("Pedido entregue com sucesso. Obrigado pela compra!")
    case _:
        print("Status não identificado. Verifique se digitou corretamente.")
