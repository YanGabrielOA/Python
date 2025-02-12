Salario = float(input("Insira o valor do seu salario: "))
Reajuste = float(input("Insira o Percentual de reajuste do seu salario: "))

Salario += Salario*(Reajuste/100)

print(f"O seu novo salario sera de: R${Salario}")

