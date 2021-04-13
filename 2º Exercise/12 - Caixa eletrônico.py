quantia = int(input("Digite quanto você deseja sacar: "))
if 10 < quantia < 600:
    notasCem, resto = quantia // 100, quantia % 100  # determina quantas notas de 100
    notasCinquenta, resto = resto // 50, resto % 50  # determina quantas notas de 50
    notasVinte, resto = resto // 20, resto % 20  # determina quantas notas de 20
    notasDez, resto = resto // 10, resto % 10  # determina quantas notas de 10
    notasCinco, resto = resto // 5, resto % 5  # determina quantas notas de 5
    notasDois, resto = resto // 2, resto % 2  # determina quantas notas de 2
    notasUm = resto // 1  # determina quantas notas de 1

    if notasCem != 0:
        print(notasCem, "notas de 100 reais")
    if notasCinquenta != 0:
        print(notasCinquenta, "notas de 50 reais")
    if notasVinte != 0:
        print(notasVinte, "notas de 20 reais")
    if notasDez != 0:
        print(notasDez, "notas de 10 reais")
    if notasCinco != 0:
        print(notasCinco, "notas de 5 reais")
    if notasDois != 0:
        print(notasDois, "notas de 2 reais")
    if notasUm != 0:
        print(notasUm, "notas de 1 real")
else:
    print("Valor de saque inválido.")