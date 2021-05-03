impar = 0
par = 0
for i in range(10):
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1
print("Você digitou", par, "números pares e", impar, "números ímpares")