matrizPascal = []

matrizPascal.append(1)
matrizPascal.append(1, 1)

for i in range(10):
    for j in range(i+1):
        if j == 1 or j == i:
            matrizPascal.append(1)
        else:
            matrizPascal.append()