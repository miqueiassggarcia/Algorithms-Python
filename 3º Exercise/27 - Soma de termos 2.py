numero = int(input("Digite quantos valores para somar: "))
soma = 0
print("H = ", end="")
for i in range(1, numero + 1):
    soma = soma + 1 / i
    if i == 1:
        print(1, end=" ")
    else:
        print("+ ", 1, "/", i, end=" ", sep="")
print()
print(soma)