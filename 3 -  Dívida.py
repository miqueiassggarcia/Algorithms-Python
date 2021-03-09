valorOriginal = float(input("Digite o valor da dívida original: "))
diasAtrasados = float(input("Digite os dias que ela está atrasada: "))
multaPorDia = float(input("Digite o valor cobrado por dia atrasado: "))
valorTotal = valorOriginal + diasAtrasados * multaPorDia
print("O valor da multa atrasada será de", valorTotal, "reais")
