numero = int(input("Digite um número entre 0 e 1000: "))
numerostr = str(numero)

if numero <= 0 or numero > 999:
    print("Número inválido.")

if len(numerostr) < 2:
    if numerostr[0] == "1":
        print(numero, "=", numero, "unidade")
    else:
        print(numero, "=", numero, "unidades")
elif len(numerostr) < 3:
    if numerostr[0] == "1":
        if numerostr[1] == "1":
            print(numero, "=", numerostr[0], "dezena e", numerostr[1], "unidade")
        else:
            print(numero, "=", numerostr[0], "dezena e", numerostr[1], "unidades")
    elif numerostr[1] == "1":
        print(numero, "=", numerostr[0], "dezenas e", numerostr[1], "unidade")
    else:
        print(numero, "=", numerostr[0], "dezenas e", numerostr[1], "unidades")
else:
    if numerostr[0] == "1":
        if numerostr[1] == "1":
            if numerostr[2] == "1":
                print(numero, "=", numerostr[0], "centena,", numerostr[1], "dezena e", numerostr[2], "unidade")
            else:
                print(numero, "=", numerostr[0], "centena,", numerostr[1], "dezena e", numerostr[2], "unidades")
        else:
            if numerostr[2] == "1":
                print(numero, "=", numerostr[0], "centena,", numerostr[1], "dezenas e", numerostr[2], "unidade")
            else:
                print(numero, "=", numerostr[0], "centena,", numerostr[1], "dezenas e", numerostr[2], "unidades")
    elif numerostr[1] == "1":
        if numerostr[2] == "1":
            print(numero, "=", numerostr[0], "centenas,", numerostr[1], "dezena e", numerostr[2], "unidade")
        else:
            print(numero, "=", numerostr[0], "centenas,", numerostr[1], "dezena e", numerostr[2], "unidades")
    else:
        if numerostr[2] == "1":
            print(numero, "=", numerostr[0], "centenas,", numerostr[1], "dezenas e", numerostr[2], "unidade")
        else:
            print(numero, "=", numerostr[0], "centenas,", numerostr[1], "dezenas e", numerostr[2], "unidades")
