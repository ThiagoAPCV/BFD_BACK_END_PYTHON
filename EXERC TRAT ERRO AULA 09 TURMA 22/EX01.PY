'''Faça um programa em Python e salve o arquivo na extensão .py que simule
uma pequena calculadora:
- O programa deve pedir dois números ao usuário.
- Depois, deve pedir a operação desejada (+, -, *, /).
- As operações devem ser implementadas em funções (ex: funcao soma, subtracao,
multiplicacao e divisao).
- Trate os seguintes casos usando try/except/else/finally:
1. Se o usuário digitar algo que não seja número → mostrar "Erro: valor inválido".
2. Se o usuário escolher "/" e o denominador for zero → mostrar "Erro: divisão por zero".
3. Se o usuário escolher uma operação inválida → mostrar "Erro: operação inválida".
4. Caso contrário → mostrar o resultado chamando a função correspondente.
- No final, use o bloco finally para exibir a mensagem "Fim do programa".'''

# Calculadora
def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

try:
    # Entrada dos números
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # Escolha da operação
    operacao = input("Digite a operação desejada (+, -, *, /): ")

    # Verificação da operação
    if operacao == "+":
        resultado = soma(num1, num2)
    elif operacao == "-":
        resultado = subtracao(num1, num2)
    elif operacao == "*":
        resultado = multiplicacao(num1, num2)
    elif operacao == "/":
        if num2 == 0:
            raise ZeroDivisionError  
        resultado = divisao(num1, num2)
    else:
        raise ValueError("operação inválida")  

except ValueError as e:
    if str(e) == "operação inválida":
        print("Erro: operação inválida")
    else:
        print("Erro: valor inválido")
except ZeroDivisionError:
    print("Erro: divisão por zero")
else:
    print(f"Resultado: {resultado}")
finally:
    print("Fim do programa")