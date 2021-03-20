produto1 = float(input("Digite o valor do primeiro produto: "))
produto2 = float(input("Digite o valor do segundo produto: "))
produto3 = float(input("Digite o valor do terceiro produto: "))
menor = produto1
if menor > produto2:
    menor = produto2
if menor > produto3:
    menor = produto3
print("O produto que você deve comprar é o que tem o preço de %.f" % menor, "reais")