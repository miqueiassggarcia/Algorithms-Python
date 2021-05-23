def quadradoMagico(matriz, ordem):
    numero = 0

    for i in range(ordem):
        numero += matriz[1][i]

    for i in range(ordem):
        coluna = 0
        linha = 0
        for j in range(ordem):
            coluna += matriz[j][i]
            linha += matriz[i][j]
        if coluna != numero or linha != numero:
            return False

    return True


ordem = int(input("Digite a ordem da sua matriz: "))

print()
matriz = []
for i in range(ordem):
    linha = []
    for j in range(ordem):
        print("Digite o ", j + 1, "º valor da linha ", i + 1, ": ", end="", sep="")
        valor = int(input())
        linha.append(valor)
    matriz.append(linha)

print()
for i in range(ordem):
    for j in range(ordem):
        print(matriz[i][j], end=" ")
    print()

if quadradoMagico(matriz, ordem):
    print("\nA matriz é um quadrado mágico.")
else:
    print("\nA matriz não é um quadrado mágico.")