num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    resultado = num1 - num2
else:
    resultado = num2 - num1

print(f"Resultado da subtração do maior pelo menor: {resultado}")
