print("Digite o código da 1ª cidade: ", sep="", end="")
codigo = int(input(""))
numeroVeiculos = int(input("Digite a quantidade de veículos da cidade: "))
numeroAcidentes = int(input("Digite a quantidade de acidentes de trânsito com vítimas: "))

maiorIndiceAcidente = numeroAcidentes / numeroVeiculos
menorIndiceAcidente = numeroAcidentes / numeroVeiculos

cidadeMaiorIndiceAcidente = codigo
cidadeMenorIndiceAcidente = codigo

totalVeiculos = 0
acidentesEspecifica = 0
contadorAcidentesEspecifica = 0

for i in range(2, 7):
    if 0 < numeroAcidentes / numeroVeiculos > maiorIndiceAcidente:
        maiorIndiceAcidente = numeroAcidentes / numeroVeiculos
        cidadeMaiorIndiceAcidente = codigo
    elif numeroAcidentes / numeroVeiculos < menorIndiceAcidente:
        menorIndiceAcidente = numeroAcidentes / numeroVeiculos
        cidadeMenorIndiceAcidente = codigo

    totalVeiculos += numeroVeiculos

    if numeroVeiculos < 2000:
        acidentesEspecifica += numeroAcidentes
        contadorAcidentesEspecifica += 1
    if i != 6:
        print("Digite o código da ", i, "ª cidade: ", sep="", end="")
        codigo = int(input(""))
        numeroVeiculos = int(input("Digite a quantidade de veículos da cidade: "))
        numeroAcidentes = int(input("Digite a quantidade de acidentes de trânsito com vítimas: "))

print('\nO maior índice de acidentes é', maiorIndiceAcidente * 100, "% que pertence a cidade de código",
      cidadeMaiorIndiceAcidente, "e o menor índice é", menorIndiceAcidente * 100, "% que pertence a cidade de código",
      cidadeMenorIndiceAcidente)
print("A média de veículos nas cinco cidades é", totalVeiculos / 5)
print("A média de acidentes de trânsito nas cidades com menos de 2.000 veículos é de", acidentesEspecifica / contadorAcidentesEspecifica)
