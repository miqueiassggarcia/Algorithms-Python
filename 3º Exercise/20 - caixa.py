valorTotal = float(input("Digite o valor da sua compra 1: "))
valor = 1
numero = 2

while valor != 0:
    print("Digite o valor da sua compra ", numero, ": ", sep="", end="")
    valor = float(input())
    valorTotal += valor
    numero += 1
print("Total: R$",valorTotal)

pagamento = float(input("Valor que vocẽ forneceu para pagar: "))

restante = pagamento - valorTotal
while restante < 0:
    restante = float(input("Tá faltando dinheiro, me dê o dinheiro todo seu vagabundo: ")) + restante

print("Seu troco será:", restante)
