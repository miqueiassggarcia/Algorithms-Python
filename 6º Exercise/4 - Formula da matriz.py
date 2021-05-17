nLinhas = 10
nColunas = 10

matriz = []

for i in range(nLinhas):
    matriz.append([0] * nColunas)

for i in range(nLinhas):
    for j in range(nColunas):
        if i < j:
            matriz[i][j] = 2*i + 7*j - 2
        elif i == j:
            matriz[i][j] = 3*i*i - 1
        else:
            matriz[i][j] = 4*i*i*i - 5*j*j + 1

for i in range(nLinhas):
    for j in range(nColunas):
        print(matriz[i][j], end=" ")
    print()
