numero = int(input("Digite um número: "))

primo = "é"

for i in range(2, numero):
    if numero % i == 0:
        print("Divisível por", i)
        primo = "não é"

print("O número", numero, primo, "primo")