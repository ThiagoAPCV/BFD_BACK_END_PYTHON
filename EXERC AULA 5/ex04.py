senha = "Python123"

# Verificação das condições
senha_valida = (
    senha != ""             # A senha não é vazia
    and len(senha) > 8      # A senha tem mais de 8 caracteres
    and senha == "Python123"  # A senha é exatamente igual a "Python123"
    and senha != "123456"     # A senha é diferente de "123456"
)

# Saída final
print(f"A senha é válida? {senha_valida}")