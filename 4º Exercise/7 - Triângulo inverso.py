ch = input("Caractere: ")
for linha in range(8):
    for coluna in range(8):
        if coluna <= 8 - linha - 1:
            print(ch, ch, sep='', end='')
        else:
            print('  ', sep='', end='')
    print()
