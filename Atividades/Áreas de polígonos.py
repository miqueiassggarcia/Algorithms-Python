import math

numeroLados = int(input("Digite o número de lados do polígono: "))
if numeroLados == 5:
    print("É um pentágono.")
else:
    medidaLado = float(input("Digite a medida do lado(em cm): "))

    if numeroLados < 3:
        print("NÃO É UM POLÍGONO.")
    elif numeroLados == 3:
        areaTriangulo = medidaLado ** 2 * math.sqrt(3) / 4
        print("É um triângulo e sua área é %.2f" % areaTriangulo, "cm²")
    elif numeroLados == 4:
        areaQuadrado = medidaLado ** 2
        print("É um quadrado e sua área é", areaQuadrado, "cm²")
    else:
        print("POLÍGONO NÃO IDENTIFICADO.")
