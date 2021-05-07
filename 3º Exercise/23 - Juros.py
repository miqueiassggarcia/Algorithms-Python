valorInicial = float(input("Digite o valor que será pago: "))
print("Valor da Dívida            Valor dos Juros        Quant. de parcelas         Valor da Parcela")
print(valorInicial, "                    0                      1                          R$", valorInicial)
parcelas = 3
for i in range(10, 26, 5):
    valor = valorInicial + valorInicial * i/100
    print(valor, "                   ", valor - valorInicial, "                ", parcelas,
          "                         R$ %.2f" % float(valor/parcelas))
    parcelas += 3
