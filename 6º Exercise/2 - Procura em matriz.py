ordem = 5
matriz = []
posicoes = []

for i in range(ordem):
    matriz.append([0] * ordem)

for i in range(ordem):
    for j in range(ordem):
        print("Digite o valor da linha ", i + 1, " e da coluna ", j + 1, ": ", sep="", end="")
        matriz[i][j] = int(input())

valorProcura = int(input("Digite um valor a ser procurado na matriz: "))

encontrou = False
for i in range(ordem):
    for j in range(ordem):
        if matriz[i][j] == valorProcura:
            print("O valor aparece na linha", i + 1, "e na coluna", j + 1)
            encontrou = True

if not encontrou:
    print("Não encontrou.")
