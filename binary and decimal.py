def todecimal():
    binary = input("Digite o binário a ser convertido: ")

    binarylenght = len(binary) - 1
    total = 0

    for i in binary:
        numero = int(i)
        if numero > 1 or numero < 0:
            quit("Esse número não é um binário")

    for i in binary:
        numero = int(i)
        total += numero * 2 ** binarylenght
        print(i, "*", 2, "^", binarylenght, "=", numero * 2 ** binarylenght)
        binarylenght -= 1
    print(total)


def tobinary():
    decimal: int = int(input("Digite o decimal para ser convertido: "))

    binary = []

    while decimal != 0:
        binary.append(decimal % 2)
        print(decimal, "/", 2, "=", decimal // 2, "resto:", decimal % 2)
        decimal //= 2
    for i in binary:
        print(i, end="")

print("Escolha qual conversão você deseja fazer,")
print("0 para converter de binário para decimal e")
print("1 para converter de binário para decimal: ")

convertto = int(input())

if convertto == 0:
    tobinary()
elif convertto == 1:
    todecimal()
else:
    print("Valor inválido")