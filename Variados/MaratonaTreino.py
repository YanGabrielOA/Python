Valor = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
Letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
Numeracao = 0
Entrada = input("Entre com o sequenciamento de proteinas: ")

for i in range(26):
    for x in Entrada:
        if(x == Letras[i]):
            Numeracao += Valor[i]

print("O valor dessa sequencia de proteinas: {}",Numeracao)
