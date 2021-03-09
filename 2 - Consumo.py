kmInicial = float(input("Digite a quilometragem inicial: "))
kmFinal = float(input("Digite a quilometragem final: "))
consumo = float(input("Digite o consumo: "))
mediaDeConsumo = (kmFinal - kmInicial) / consumo
print("A média de consumo é de", mediaDeConsumo, "Km/l")
