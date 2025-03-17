
metros = float(input("Digite a medida em metros: "))


print("Escolha a conversão:")
print("1 - Decímetros")
print("2 - Centímetros")
print("3 - Milímetros")


opcao = int(input("Digite a opção: "))


if opcao == 1:
    resultado = metros * 10.0
    print(f"{metros} metros equivalem a {resultado} decímetros.")
elif opcao == 2:
    resultado = metros * 100.0
    print(f"{metros} metros equivalem a {resultado} centímetros.")
elif opcao == 3:
    resultado = metros * 1000.0
    print(f"{metros} metros equivalem a {resultado} milímetros.")
else:
    print("Opção inválida!")
