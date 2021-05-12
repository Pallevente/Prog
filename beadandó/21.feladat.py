import string

lista = []
ossz = 0


def kedvezmenyes(string):
    mgh_szam = 0
    atlag = 0
    mgh = "aeiouöü"

    for i in range(0, len(lista)):
        for j in mgh:
            atlag += lista[i][0].lower().count(j)
    atlag = atlag / len(lista)

    for j in mgh:
        mgh_szam += string.lower().count(j)

    if mgh_szam > atlag:
        return True
    else:
        return False


while True:
    szo = input("Kérem a termék nevét, darabszámát és egységárát!(!!Szóközzel elválasztva!!):")
    if szo == "vasarlas vege":
        break
    a = szo.split(" ")
    lista.append(a)

for i in range(0, len(lista)):
    if kedvezmenyes(lista[i][0]):
        print(lista[i][1] + "db " + lista[i][0] + " - " + lista[i][1] + " * " + str(
            int(lista[i][2]) * 0.9) + "Ft (10% kedvezmeny)")
        ossz += round(int(lista[i][1]) * (int(lista[i][2]) * 0.9),0)
    else:
        print(lista[i][1] + "db " + lista[i][0] + " - " + lista[i][1] + " * " + lista[i][2] + "Ft")
        ossz += round(int(lista[i][1]) * int(lista[i][2]),0)

print("---")
print("Vegosszeg: " + str(ossz) + "Ft")



















