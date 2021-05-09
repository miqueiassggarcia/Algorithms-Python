tamanho = int(input("Digite o tamanho do vetor: "))
vetor = [0] * tamanho
vetorImpar = [0] * tamanho
vetorPar = [0] * tamanho
passoImpar = 0
passoPar = 0

for i in range(tamanho):
    print("Digite o valor ", i + 1, ": ", sep="", end="")
    vetor[i] = int(input())

for i in range(tamanho):
    if vetor[i] % 2 == 0:
        vetorPar[passoPar] = vetor[i]
        passoPar += 1
    else:
        vetorImpar[passoImpar] = vetor[i]
        passoImpar += 1

print("O vetor inicial era: ", vetor)

print("A parte ímpar do vetor é: [", end="")
for i in range(passoImpar):
    if i == passoImpar - 1:
        print(vetorImpar[i], "]", sep="")
    else:
        print(vetorImpar[i], ", ", sep="", end="")

print("A parte par do vetor é: [", end="")
for i in range(passoPar):
    if i == passoPar - 1:
        print(vetorPar[i], "]", sep="")
    else:
        print(vetorPar[i], ", ", sep="", end="")
