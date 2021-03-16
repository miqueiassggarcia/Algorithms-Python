import datetime

nome = input("Digite o seu nome: ")
anoNascimento = int(input("Digite o ano do seu nascimento: "))
idade = datetime.datetime.today().year - anoNascimento
print(nome, "tem ou fará %.f" % idade, "anos")
