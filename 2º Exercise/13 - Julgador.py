questao1 = input("Telefonou para a vítima?(S/N): ")
questao2 = input("Esteve no local do crime?(S/N): ")
questao3 = input("Mora perto da vítima?(S/N): ")
questao4 = input("Devia para a vítima?(S/N): ")
questao5 = input("Já trabalhou com a vítima?(S/N): ")

if questao2 == "S":
    print("Você está classificado(a) como suspeito(a).")
if questao3 == "S" or questao4 == "S":
    print("Você está classificado(a) como cúmplice.")
if questao5 == "S":
    print("Você está classificado(a) como assassino(a).")
if questao2 == "N" and questao3 == "N" and questao4 == "N" and questao5 == "N":
    print("Você está classificado(a) como inocente")
