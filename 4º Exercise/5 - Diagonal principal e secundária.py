ch = input("Caractere: ")
for linha in range(8):
    for coluna in range(8):
        if linha == coluna or coluna + linha == 7:
            print(ch, ch, sep='', end='')
        else:
            print('  ', sep='', end='')
    print()
