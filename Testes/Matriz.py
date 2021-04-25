linhas = int(input("Digite quantas linhas terá a matriz: "))
colunas = int(input("Digite quantas colunas terá a matriz: "))

for linha in range(1, linhas + 1):
    for coluna in range(1, colunas + 1):
        print(linha, ".", coluna, sep="", end=" ")
    print()
