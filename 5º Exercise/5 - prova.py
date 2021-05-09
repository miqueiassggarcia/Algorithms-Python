print("Gabarito: ")
nQuestoes = 10
gabarito = [0] * nQuestoes

for i in range(nQuestoes):
    print("Questão ", i + 1, ": ", end="", sep="")
    gabarito[i] = input()

nAlunos = int(input("Quantos alunos há na turma? "))

for aluno in range(nAlunos):
    resposta = [0] * nQuestoes
    print("Aluno", aluno+1)
    for questao in range(nQuestoes):
        print("Resposta da questão ", questao+1, ": ", end="", sep="")
        resposta[questao] = input()
    cont = 0
    for questao in range(nQuestoes):
        if gabarito[questao] == resposta[questao]:
            cont = cont + 1
    if cont == 1:
        print("O aluno", aluno + 1, "acertou 1 questão.")
    else:
        print("O aluno", aluno+1, "acertou", cont, "questões.")
