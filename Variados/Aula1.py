ValorProduto = float(input("Digite o valor do produto: "))
Desconto = float(input("Digite o desconto em %: "))

ValorDesconto  = ValorProduto * (Desconto/100)

ValorVenda =  ValorProduto - ValorDesconto

print(f"O Valor Final do Produto é {ValorVenda}")