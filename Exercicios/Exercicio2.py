VP = float(input("Digite o valor da prestação: "))
TJ = float(input("Digite o valor da taxa de juros: "))
TP = int(input("Digite quantos meses a prestação esta atrasada: "))

Valor = VP+(VP*(TJ/100)*TP)

print(f"O valor da prestação é atualmente R${Valor:.2f}")