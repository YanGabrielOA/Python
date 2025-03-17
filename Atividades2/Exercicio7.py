nome_cliente = input("Digite o nome do cliente: ")
deposito = float(input("Digite o valor do depósito: "))

saldo_atual = 800 + deposito

if saldo_atual == 0:
    mensagem = "Saldo Limite"
elif saldo_atual > 0:
    mensagem = "Saldo Positivo"
else:
    mensagem = "Saldo Negativo"

print(f"Cliente: {nome_cliente}")
print(f"Saldo Atual: R$ {saldo_atual:.2f}")
print(mensagem)
