import math
valorDeA = float(input("Digite o valor de a: "))
valorDeB = float(input("Digite o valor de b: "))
valorDeC = float(input("Digite o valor de c: "))

delta = valorDeB ** 2 - 4 * valorDeA * valorDeC
if delta < 0:
    quit("∆ < 0, não existe raiz real para delta negativo")
if delta == 0:
    print("∆ = 0, raízes iguais.")
x1 = (- valorDeB + math.sqrt(delta)) / 2 * valorDeA
x2 = (- valorDeB - math.sqrt(delta)) / 2 * valorDeA

print("As raízes da sua equação são X1 =", x1, "e X2 =", x2)
