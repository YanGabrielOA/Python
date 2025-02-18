from datetime import datetime #Vou usar essa biblioteca pra ficar mais completinho sor

Nome = input("Digite Seu Nome: ")
DataNascimento = datetime.strptime(input("Informe sua data de nascimento no formato dd/mm/aaaa: "),"%d/%m/%Y")
Idade = (datetime.now() - DataNascimento).days//365

print(f"{Nome} possui {Idade} anos de vida")