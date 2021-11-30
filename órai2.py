#1. Írjon programot, mely kiírja a képernyőre a 1-10 ig a számok reciprokát!

for szam in range(1,11,1):
    reciprok=1/szam
    print(reciprok)

#2. írj programot, mely beolvassa a hatvány alapját és a kitevőt, és kiírja a hatványértéket!

alap=int(input("Adja meg a hatvány alapját: "))
kitevo=int(input("Adja meg a hatványkitevőt: "))
hatvanyertek=alap**kitevo
print("A hatványérték: {0}" .format(hatvanyertek))
