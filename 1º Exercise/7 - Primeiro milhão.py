salarioMensal = float(input("Digite o salário mensal: "))
dispesas = float(input("Digite as suas despesas mensais: "))
tempoMeses = 1000000 // (salarioMensal - dispesas)
tempoAnos = tempoMeses / 12
print("O tempo gasto para que você atinga o primeiro milhão seria %.f" % tempoMeses, "meses, ou, em anos %.1f" % tempoAnos)
