valor_compra = float(input("Digite o valor da compra do produto: "))

if valor_compra < 20.00:
    valor_venda = valor_compra * 1.45
else:
    valor_venda = valor_compra * 1.30

print(f"O valor de venda do produto será: R$ {valor_venda:.2f}")
