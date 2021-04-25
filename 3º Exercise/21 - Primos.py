quantidade = int(input("Digite o espaço de verificação: "))

for numero in range(1, quantidade + 1):
    primo = True
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
    if primo:
        print(numero, end=" ")
