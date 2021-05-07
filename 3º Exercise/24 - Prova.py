print("Preencha os valores do gabarito.")
gabarito = [""] * 10
for i in range(10):
    print("Digite a resposta da questão ", i+1, ": ", sep="", end="")
    gabarito[i] = input().upper()


totalNotas = 0
maiorNota = 0
menorNota = 10000000000000000000000
totalAlunos = 0
repetir = "S"

while repetir == "S":
    print("\nPreencha as respostas.")
    nota = 0
    for i in range(10):
        print("Digite a alternativa da questão ", i + 1, ": ", sep="", end="")
        valor = input().upper()
        if valor == gabarito[i]:
            nota += 1
    if maiorNota < nota:
        maiorNota = nota
    if menorNota > nota:
        menorNota = nota
    totalNotas += nota
    totalAlunos += 1
    print("Sua nota foi", nota)
    repetir = input("Outro aluno vai usar o sistema(S/N): ").upper()

print("\nA maior nota foi ", maiorNota, ", a menor nota foi ", menorNota, ".\nO total de alunos que usou o sistema foi ",
      totalAlunos, ".\nA média das notas foi ", totalNotas / totalAlunos, ".", sep="")
