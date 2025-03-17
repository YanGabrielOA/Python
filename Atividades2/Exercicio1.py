ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))


idade = ano_atual - ano_nascimento


if idade >= 16:
    print(f"Você tem {idade} anos e PODE votar este ano.")
else:
    print(f"Você tem {idade} anos e NÃO PODE votar este ano.")