from random import randrange

tamanhoMatriz = int(input("Informe a ordem da matriz: "))
matriz = []

for i in range(tamanhoMatriz):
    matriz.append([0] * tamanhoMatriz)

for i in range(tamanhoMatriz):
    for j in range(tamanhoMatriz):
#        print("M[", i+1, ",", j+1, "]: ", sep="", end="")
        matriz[i][j] = randrange(0, 10)

for i in range(tamanhoMatriz):
    for j in range(tamanhoMatriz):
        print(matriz[i][j], end=" ")
    print()

coluna1 = int(input("Digite qual coluna você deseja trocar: ")) - 1
coluna2 = int(input("Digite por qual coluna será mudada: ")) - 1

reserva = 0
for i in range(tamanhoMatriz):
    reserva = matriz[i][coluna1]
    matriz[i][coluna1] = matriz[i][coluna2]
    matriz[i][coluna2] = reserva

for i in range(tamanhoMatriz):
    for j in range(tamanhoMatriz):
        print(matriz[i][j], end=" ")
    print()
