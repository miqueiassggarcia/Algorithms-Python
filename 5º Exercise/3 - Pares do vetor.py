vetor = [0] * 10
quantidade = 0

for i in range(10):
    print("Digite o valor ", i + 1,": ", sep="", end="")
    vetor[i] = int(input())

for i in range(10):
    if vetor[i] % 2 == 0:
        quantidade += 1

print("\nO vetor possui", quantidade, "valores pares")