quanTurmas = int(input("Digite a quantidade de turmas: "))
quanAlunos = 0

for i in range(1, quanTurmas + 1):
    print("Digite a quantidade de alunos da turma ", i, ": ", sep="", end="")
    alunos = int(input())
    if alunos < 1 or alunos > 40:
        while alunos < 1 or alunos > 40:
            alunos = int(input("Uma turma não pode ter mais de 40 alunos ou menos de 1, tente novamente: "))
    quanAlunos = quanAlunos + alunos

media = quanAlunos / quanTurmas

print("A média de alunos por turma é de", media, "alunos")
