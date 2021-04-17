PaisA = 80000
TaxaA = 0.3
PaisB = 200000
TaxaB = 0.015
anos = 0

while PaisA < PaisB:
    PaisA += PaisA * TaxaA
    PaisB += PaisB * TaxaB
    anos += 1

print("Levarão", anos, "anos para que o país ")