numero = int(input("Digite quantos termos serão somados: "))
soma = 0
print("S = ", end="")
for i in range(1, numero + 1):
    soma = soma + i / (2 * i - 1)
    if i == numero:
        print(i, "/", 2 * i - 1, end="", sep="")
    else:
        print(i, "/", 2 * i - 1, end=" + ", sep="")
print()
print(soma)