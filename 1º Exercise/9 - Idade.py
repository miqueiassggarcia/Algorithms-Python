import datetime

nome = input("Digite o seu nome: ")
anoNascimento = int(input("Digite as suas despesas mensais: "))
idade = datetime.datetime.today().year - anoNascimento
print(nome, "tem %.f" % idade, "anos")