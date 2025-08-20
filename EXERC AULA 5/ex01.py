tem_wifi = False
tem_dados_moveis = True

# Verificação lógica com OR
pode_conectar = tem_wifi or tem_dados_moveis

print(f"O celular pode se conectar à internet? {pode_conectar}")