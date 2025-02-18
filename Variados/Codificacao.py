Letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



y = int 



def Codificar(Texto,FDC):
    Codificado = ""
    for x in Texto:
        for i in range(26):
            if x  == Letras[i]:
                  Codificado += Letras[i+FDC]

    return Codificado

def Decodificar(Texto,FDC):
     Decodificado = ""
     for x in Texto:
          for i in range(26):
               if x == Letras[i]:
                    Decodificado += Letras[i-FDC]
     return Decodificado

while y != 0:
   op = int(input("Digite a opção: \n1 - Codificar\n2 - Decodificar\n0 - Sair\n"))
   match op:
        case 1:
             FDC = int(input("Digite o fator de comunicacao: "))
             Texto = input("Digite o texto a ser codificado: ")
             
             print(Codificar(Texto,FDC))
             
        case 2: 
             FDC = int(input("Digite o fator de comunicacao: "))
             Texto = input("Digite o texto a ser codificado: ")
             
             print(Decodificar(Texto,FDC))
             
        case 0:
             y = 0
             
        case _:
             print("OPCAO INVALIDA")
                 


