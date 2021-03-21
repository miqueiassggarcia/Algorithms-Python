litrosVendidos = float(input("Digite a quantidade de litros que você abasteçeu: "))
tipo = input("Digite qual tipo de combustível foi abastecido(G para gasolina/A para álcool): ")

if tipo == "G":
    if 0 < litrosVendidos <= 20:
        valor = litrosVendidos * (4.5 - 4.5 * 0.04)
        print("O valor será de %.2f" % valor, "reais")
    elif litrosVendidos > 20:
        valor = litrosVendidos * (4.5 - 4.5 * 0.06)
        print("O valor será de %.2f" % valor, "reais")
elif tipo == "A":
    if 0 < litrosVendidos <= 20:
        valor = litrosVendidos * (3.4 - 3.4 * 0.03)
        print("O valor será de %.2f" % valor, "reais")
    elif litrosVendidos > 20:
        valor = litrosVendidos * (3.4 - 3.4 * 0.05)
        print("O valor será de %.2f" % valor, "reais")
