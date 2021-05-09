lista = []
valor = int(input("Digite um valor: "))
while valor != 0:
    lista.append(valor)
    valor = int(input("Digite um valor: "))
print(lista)
valor = int(input("Digite o número que deseja excluir: "))
# for i in range(lista.count(valor)):
#    lista.remove(valor)

while valor in lista:
    lista.remove(valor)
print(lista)
