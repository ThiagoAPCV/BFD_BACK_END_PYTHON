"""Crie um arquivo .py. Defina uma senha correta, por exemplo, "python123". Peça ao usuário
para digitar uma senha. Use um laço while que continue pedindo a senha enquanto ela for
diferente da senha correta. Quando a senha estiver certa, exiba uma mensagem de
sucesso.
Obs: Utilize input() para capturar a senha e print() para exibir as mensagens."""

senha_correta = "python123"

senha_digitada = input("Digite a senha: ")

while senha_digitada != senha_correta:
    print("Senha incorreta. Tente novamente.")
    senha_digitada = input("Digite a senha: ")

print("Acesso concedido. Bem-vindo!")
