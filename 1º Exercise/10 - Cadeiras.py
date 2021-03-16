comprimentoSala = float(input("Digite o comprimento da sala: "))
larguraSala = float(input("Digite o largura da sala: "))
comprimentoCadeira = float(input("Digite o comprimento da cadeira: "))
larguraCadeira = float(input("Digite o largura da cadeira: "))

if comprimentoSala < 1.5:
    quit("Sua sala é pequena de mais para colocar cadeiras")
if larguraSala < larguraCadeira:
    quit("a largura é muito pequena para essa cadeira")
if (comprimentoSala - 1.5) < comprimentoCadeira:
    quit("O comprimento é muito pequena para essa cadeira")

quantidadeColunas = (larguraSala + 0.5) // (larguraCadeira + 0.5)
quantidadeLinhas = (comprimentoSala - 1.5 + 0.2) // (comprimentoCadeira + 0.2)

print("A quantidade de cadeiras que cabem na sala é %.f" % (quantidadeColunas * quantidadeLinhas))