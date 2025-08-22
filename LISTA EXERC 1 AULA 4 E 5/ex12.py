# Programa para verificar se o celular pode se conectar à internet

tem_wifi = False
tem_dados_moveis = True

pode_conectar = tem_wifi or tem_dados_moveis

print(f"O celular pode se conectar à internet? {pode_conectar}")