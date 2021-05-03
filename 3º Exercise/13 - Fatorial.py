valor = int(input("Digite um número para calcular o fatorial: "))
fatorial = 1
for i in range(valor, 1, -1):
    fatorial = fatorial * i
print("O fatorial é", fatorial)
print(len(str(fatorial)))
