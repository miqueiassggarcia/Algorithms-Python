tamanhoMatriz = int(input("Informe a ordem da matriz: "))
matriz = []

for i in range(tamanhoMatriz):
    matriz.append([0] * tamanhoMatriz)

for i in range(tamanhoMatriz):
    for j in range(tamanhoMatriz):
        print("M[", i+1, ",", j+1, "]: ", sep="", end="")
        matriz[i][j] = int(input())

for i in range(tamanhoMatriz):
    for j in range(tamanhoMatriz):
        print(matriz[i][j], end=" ")
    print()

soma = 0

for i in range(tamanhoMatriz):
    for j in range(i+1, tamanhoMatriz):
            soma += matriz[i][j]

print("O valor da soma da diagonal principal é", soma)
