nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
if 7 <= media <= 10:
    print("Aprovado")
elif 7 > media >= 5:
    print("Prova final")
elif 5 > media > 0:
    print("Reprovado")
else:
    print("Média inválida, tente novamente")
