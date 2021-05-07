numLista = int(input("Digite o tamanho da lista: "))

lista1 = [0] * numLista
lista2 = [0] * numLista

igual = True

print("Lista 1:")
for i in range(numLista):
    print("Elemento ", i+1, ": ", sep="", end="")
    lista1[i] = int(input())
print("Lista 2")
for i in range(numLista):
    print("Elemento ", i+1, ": ", sep="", end="")
    lista2[i] = int(input())

for i in range(numLista):
    if lista1[i] != lista2[i]:
        igual = False

# if lista2 == lista1: no python é possível comparar arrays
    print("As listas são iguais")
else:
    print("As listas não são iguais")
