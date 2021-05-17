ordem = 4
matriz = []
for i in range(ordem):
    matriz.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        print("Digite o valor da linha ", i + 1, " e coluna ", j + 1, ": ", sep="", end="")
        matriz[i][j] = int(input())

quantidade = 0

for i in range(4):
    for j in range(4):
        if matriz[i][j] > 10:
            quantidade += 1
if quantidade == 1:
    print("A matriz tem", quantidade, "elemento maior de dez")
else:
    print("A matriz tem", quantidade, "elementos maiores de dez")
