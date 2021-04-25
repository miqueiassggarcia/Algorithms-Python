valor = int(input("Digite um valor(de 0 à 10): "))
while valor < 0 or valor > 10:
    valor = int(input("Valor inválido, tente novamente: "))
print("Você digitou", valor)