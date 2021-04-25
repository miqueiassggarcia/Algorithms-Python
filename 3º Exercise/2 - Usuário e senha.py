usuario = input("Digite um nome de usuário: ")
senha = input("Digite uma senha: ")
while usuario == senha:
    print("Senha igual ao nome de usuário, digite uma senha diferente do seu usuário")
    senha = input("Digite uma nova senha: ")
print("Usuário cadastrado!")
