vetor = [0] * 10
vetorAoQuadrado = [0] * 10

for i in range(10):
    print("Digite o valor ", i + 1,": ", sep="", end="")
    vetor[i] = int(input())

for i in range(10):
    vetorAoQuadrado[i] = vetor[i] * vetor[i]

print(vetor)
print(vetorAoQuadrado)