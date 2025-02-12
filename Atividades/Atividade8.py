import math
num1 = int(input("Digite o valor do numero 1:"))
num2 = int(input("Digite o valor do numero 2:"))
num3 = int(input("Digite o valor do numero 3:"))

numero = num1+num2+num3
numero = math.pow(numero,2)

print(f"O Quadrado da Soma desses numeros é: {numero}")