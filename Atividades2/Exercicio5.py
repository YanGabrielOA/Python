nome1 = input("Digite o nome da primeira pessoa: ")
altura1 = float(input("Digite a altura da primeira pessoa (em metros): "))
idade1 = int(input("Digite a idade da primeira pessoa: "))

nome2 = input("Digite o nome da segunda pessoa: ")
altura2 = float(input("Digite a altura da segunda pessoa (em metros): "))
idade2 = int(input("Digite a idade da segunda pessoa: "))

if altura1 > altura2:
    print(f"A pessoa mais alta é {nome1}, com {altura1}m de altura e {idade1} anos.")
else:
    print(f"A pessoa mais alta é {nome2}, com {altura2}m de altura e {idade2} anos.")
