quilosMorangos = float(input("Digite quantos quilos de morango você quer comprar: "))
quilosMacas = float(input("Digite quantos quilos de maçã você quer comprar: "))

valorMorangos = 0
valorMacas = 0

if 0 < quilosMorangos <= 5:
    valorMorangos = quilosMorangos * 2.5
elif quilosMorangos > 5:
    valorMorangos = quilosMorangos * 2.2

if 0 < quilosMorangos <= 5:
    valorMacas = quilosMacas * 1.8
elif quilosMorangos > 5:
    valorMacas = quilosMacas * 1.5

valorTotal = valorMacas + valorMorangos

if quilosMorangos + quilosMacas > 8 or valorTotal > 25:
    valorTotal = valorTotal - valorTotal * 0.10

print("O valor a ser pago será %.2f" % valorTotal, "reais")
