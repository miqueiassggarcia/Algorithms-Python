quantCds = int(input("Digite a quantidade de CDs da sua coleção: "))

valorTotal = 0

for i in range(1, quantCds + 1):
    print("Digite o valor do cd ", i, ": ", sep="", end="")
    valor = float(input())
    valorTotal += valor
print("O valor total gasto foi de", valorTotal, "e o valor médio gasto por CD é de", valorTotal / quantCds)
