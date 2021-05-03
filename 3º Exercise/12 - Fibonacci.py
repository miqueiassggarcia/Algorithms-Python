valor1 = 1
valor2 = 1
print(valor1,", ", valor2, sep="", end="")
for i in range(20):
    print(", ", valor1 + valor2, sep="", end="")
    if valor1 <= valor2:
        valor1 = valor2 + valor1
    else:
        valor2 = valor2 + valor1