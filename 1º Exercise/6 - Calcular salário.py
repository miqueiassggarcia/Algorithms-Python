salarioAtual = float(input("Digite o salário atual: "))
reajuste = float(input("Digite o percentual de reajuste: "))
novoSalario = salarioAtual + (salarioAtual * (reajuste / 100))
print("O novo salário é %.2f" % novoSalario, "reais")
