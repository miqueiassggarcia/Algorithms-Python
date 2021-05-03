valor = float(input("Digite um valor(0 para encerrar): "))
somaValores = 0
numeroDeValores = 0
while valor != 0:
    somaValores += valor
    numeroDeValores += 1
    valor = float(input("Digite um valor(0 para encerrar): "))
print("A média dos valores é ", somaValores / numeroDeValores)
