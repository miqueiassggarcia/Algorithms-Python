quantidadeTotal = 0
fechar = "N"
while fechar == "N":
    novaCompra = "S"
    valorTotal = int(input("Digite o valor da compra: "))
    while novaCompra == "S":
        novaCompra = input("Há mais itens a serem processados?(S/N) ").upper()
        if novaCompra == "S":
            valorTotal += int(input("Digite o valor da compra: "))
    print("O valor total da compra é R$",valorTotal, sep="")
    quantidadeTotal += valorTotal
    fechar = input("O caixa deve ser fechado?(S/N)").upper()
print("O valor total arrecadado pelo caixa foi R$", quantidadeTotal, sep="")
