valorHora = float(input("Digite o valor da sua hora: "))
quantHoras = float(input("Digite a quantidade de horas de trabalho: "))
salarioBruto = valorHora * quantHoras
if 0 < salarioBruto <= 900:
    descontoIr = 100
elif salarioBruto <= 1500:
    descontoIr = 5
elif salarioBruto <= 2500:
    descontoIr = 10
else:
    descontoIr = 20
ir = salarioBruto * (descontoIr / 100)
sindicato = salarioBruto * (3/100)
fgts = salarioBruto * (11/100)
desconto = fgts - sindicato
if descontoIr == 100:
    descontoIr = "Isento"

print("Sálario Bruto: (", quantHoras, "*", valorHora, ")                       : R$", salarioBruto)
print("(-) IR (", descontoIr, "%)                                       : R$", ir)
print("(-) Sindicato ( 3% )                                 : R$", sindicato)
print("FGTS ( 11% )                                         : R$", fgts)
print("Total de descontos                                   : R$", desconto)
print("Salário Líquido                                      : R$", salarioBruto - desconto)
