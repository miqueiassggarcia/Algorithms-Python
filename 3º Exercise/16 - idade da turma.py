idade = int(input("Digite sua idade(-1 para parar): "))
total = 0
quantidade = 0
while idade != -1:
    total += idade
    quantidade += 1
    idade = int(input("Digite sua idade(-1 para parar): "))
if 0 < total / quantidade < 26:
    facha = "uma turma jovem"
elif total / quantidade < 60:
    facha = "uma turma adulta"
else:
    facha = "uma turma idoso"
print("A média de idade da turma é %.1f" % (total / quantidade), "isso classifica a turma como", facha)
