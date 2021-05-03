maior = int(input("Digite um número: "))
for i in range(9):
    valor = int(input("Digite um número: "))
    if maior < valor:
        maior = valor
print("O maior valor digitado foi", maior)
