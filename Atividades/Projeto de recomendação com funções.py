tam = 10
filmes = [""] * tam
filmesVistos1 = []
filmesVistos2 = []

print("===================Faça o cadastro dos filmes====================")
for i in range(tam):
    print("Cadastre o ", i + 1, "º filme: ", sep="", end="")
    filmes[i] = input()


def requisitar(filmesVistos, numeroUsuario):
    print("\n\n============================Usuário ", numeroUsuario, "============================", sep="")

    for i in range(tam):
        print("Você já viu o filme ", filmes[i], "?(S/N) ", end="", sep="")
        if input().upper() == "S":
            filmesVistos.append(True)
        else:
            filmesVistos.append(False)


requisitar(filmesVistos1, 1)
requisitar(filmesVistos2, 2)


def recomendacoes(filmesVistos, comparacao, numeroUsuario):
    print("\n\n=====================Recomendações Usuário ", numeroUsuario, "=====================", sep="")

    haRecomendados = False
    for i in range(tam):
        if not filmesVistos[i] and comparacao[i]:
            print(filmes[i])
            haRecomendados = True

    if not haRecomendados:
        print("Não há recomendações")


recomendacoes(filmesVistos1, filmesVistos2, 1)
recomendacoes(filmesVistos2, filmesVistos1, 2)
