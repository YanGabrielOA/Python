CI= float(input("Digite o custo inicial de produção de um carro: "))
CF = CI +(CI*(28/100))+(CI*(45/100))
print(f"O valor final do carro vai ser de R${CF:.2f}")