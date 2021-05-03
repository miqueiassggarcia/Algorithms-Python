base = int(input("Digite a base: "))
expoente = int(input("Digite um expoente: "))

potencia = 1

for i in range(expoente):
    potencia *= base

print("O resultado é", potencia)
