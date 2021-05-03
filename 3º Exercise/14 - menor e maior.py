valor = int(input("Digite um valor(-1 para parar): "))
menor = valor
maior = valor
while valor != -1:
    if menor > valor:
        menor = valor
    if maior < valor:
        maior = valor
    valor = int(input("Digite um valor: "))
print("O maior número digitado foi", maior, "e o menor número digitado foi", menor)
