valorGasolina = input("Digite o valor da gasolina: ")
valorPago = input("Digite quanto em dinhiro que será abastecido: ")
litros = float(valorPago)/float(valorGasolina)
print("Será abastecido %.1f" % litros, "litros de gasolina")
