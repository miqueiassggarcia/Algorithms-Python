vetor = [0] * 10
print("Digite o valor 1: ", sep="", end="")
vetor[0] = int(input())
maior = vetor[0]
posicao = 0

for i in range(1, 10):
    print("Digite o valor ", i + 1, ": ", sep="", end="")
    vetor[i] = int(input())

for i in range(1, 10):
    if vetor[i] > maior:
        maior = vetor[i]
        posicao = i

print(vetor)
print("O maior elemento do vetor é", maior, "que está na posição", posicao)
