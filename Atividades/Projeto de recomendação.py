tam = 10
filmes = [""] * tam

print("===================Faça o cadastro dos filmes====================")
for i in range(tam):
    print("Cadastre o ", i + 1, "º filme: ", sep="", end="")
    filmes[i] = input()

filmesVistos1 = []
filmesVistos2 = []

print("\n\n============================Usuário 1============================")

for i in range(tam):
    print("Você já viu o filme ", filmes[i], "?(S/N) ", end="", sep="")
    if input().upper() == "S":
        filmesVistos1.append(True)
    else:
        filmesVistos1.append(False)

print("\n\n============================Usuário 2============================")

for i in range(tam):
    print("Você já viu o filme ", filmes[i], "?(S/N) ", end="", sep="")
    if input().upper() == "S":
        filmesVistos2.append(True)
    else:
        filmesVistos2.append(False)

print("\n\n=====================Recomendações Usuário 1=====================")

haRecomendados = False
for i in range(tam):
    if not filmesVistos1[i] and filmesVistos2[i]:
        print(filmes[i])
        haRecomendados = True

if not haRecomendados:
    print("Não há recomendações")

print("\n\n=====================Recomendações Usuário 2=====================")

haRecomendados = False
for i in range(tam):
    if not filmesVistos2[i] and filmesVistos1[i]:
        print(filmes[i])
        haRecomendados = True

if not haRecomendados:
    print("Não há recomendações")
