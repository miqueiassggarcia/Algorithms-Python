tam = 10
lista = [0] * tam

for i in range(tam):
    print("Digite o valor ", i + 1, ": ", sep="", end="")
    lista[i] = int(input())

print(lista)

for i in range(0, tam, 1):
    naoApareceu = True
    if i != tam - 1:
        j = i + 1
        while lista[i] != lista[j] and j < tam - 1:
            j = j + 1
        if i != 0:
            u = i - 1
            while u > -1:
                if lista[i] == lista[u]:
                    naoApareceu = False
                u -= 1
        if lista[i] == lista[j] and naoApareceu:
            print(lista[i], "se repete")
