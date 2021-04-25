maiorIdade = 0
quantidade = 0
idade = 0
print("Cadastre os dados:")
while idade != -1:
    idade = int(input("Idade(-1 para gerar resultados): "))
    if idade != -1:
        sexo = input("Sexo(M=masculino, F=feminino): ").upper()
        corOlho = input("Cor do olho(A=azul, V=verde, C=castanhos): ").upper()
        corCabelo = input("Cor do cabelo(L=louros, C=castanhos, P=pretos): ").upper()
        if maiorIdade < idade:
            maiorIdade = idade
        if sexo == "F" and 17 < idade < 36 and corOlho == "V" and corCabelo == "L":
            quantidade += 1
    print("\nCadastre novos dados:")
print("A maior idade entre os habitantes é", maiorIdade,
      "e a quantidade mulheres de idade entre 18 e 35 anos, com olhos verdes e cabelos loiros é", quantidade)
