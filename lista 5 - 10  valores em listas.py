tam = 3
lista = [0] * tam

for i in range(tam):
    print("Digite o valor ", i, ": ", sep="", end="")
    lista[i] = int(input())

print(lista)

for i in range(0, tam, 1):
    j = i + 1
    while lista[i] != lista[j] and j < tam - 1:
        j = j + 1
    if lista[i] == lista[j]:
        print(lista[i], "se repete")
