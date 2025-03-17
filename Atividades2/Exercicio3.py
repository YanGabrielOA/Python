num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

operador = input("Digite a operação (+, -, *, /): ")

if operador == "+":
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operador == "-":
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif operador == "*":
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida!")
else:
    print("Operação inválida!")
