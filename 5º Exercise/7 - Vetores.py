tam = 5
vetor1 = [0] * tam
vetor2 = [0] * tam
diferenca = [0] * (tam * 2)
passoDiferenca = 0
soma = [0] * tam
multiplicacao = [0] * tam


print("Preencha a primeira lista.")
for i in range(tam):
    print("Digite o valor ", i + 1, ": ", sep="", end="")
    vetor1[i] = int(input())

print("Preencha a segunda lista.")
for i in range(tam):
    print("Digite o valor ", i + 1, ": ", sep="", end="")
    vetor2[i] = int(input())

for i in range(tam):
    if vetor1[i] != vetor2[i]:
        diferenca[passoDiferenca] = vetor1[i]
        passoDiferenca += 1
        diferenca[passoDiferenca] = vetor2[i]
        passoDiferenca += 1

    soma[i] = vetor1[i] + vetor2[i]
    multiplicacao[i] = vetor1[i] * vetor2[i]

print("Vetores originais:\n  ", vetor1, "\n  ", vetor2)
print("Os valores que diferem entre os dois vetores é: [", sep="", end="")
for i in range(passoDiferenca):
    if i != passoDiferenca - 1:
        print(diferenca[i], ", ", sep="", end="")
    else:
        print(diferenca[i], "]", sep="")
print("Os dois vetores somados resultam em:", soma)
print("Os dois vetores multiplicados resultam em:", multiplicacao)
