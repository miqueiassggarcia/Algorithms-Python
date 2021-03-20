numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um número: "))
numero3 = float(input("Digite um número: "))
maior = numero1
menor = numero1
if maior < numero2:
    maior = numero2
    menor = numero1
if maior < numero3:
    maior = numero3
if menor > numero2:
    menor = numero2
if menor > numero3:
    menor = numero3
print("O maior número é", maior)
print("O menor número é", menor)
