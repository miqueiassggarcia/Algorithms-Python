def area(numero):
    global areaFinal
    largura = float(input("Digite a largura do " + numero + " cômodo: "))
    comprimento = float(input("Digite o comprimento do " + numero + " primeiro cômodo: "))
    areaComodo = largura * comprimento
    if numero == "primeiro":
        areaFinal = areaComodo
        return print("A área do", numero, "cômodo é", areaComodo, "m²")
    if numero == "quarto":
        areaFinal += areaComodo
        return print("A área do", numero, "cômodo é", areaComodo, "e a área total é", areaFinal, "m²")
    areaFinal += areaComodo
    return print("A área do", numero, "cômodo é", areaComodo, "m²")


area("primeiro")
area("segundo")
area("terceiro")
area("quarto")
