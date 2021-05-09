tam = 10
vetor = [0] * tam
vetorInverso = [0] * tam
passo = tam - 1

for i in range(tam):
    print("Digite o valor ", i + 1, ": ", sep="", end="")
    vetor[i] = int(input())
    vetorInverso[passo] = vetor[i]
    passo -= 1

print("O vetor criado foi:",vetor)
print("O vetor inverso é:",vetorInverso)