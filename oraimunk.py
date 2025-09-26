nev = input("Add meg a teljes neved: ")
szavak = nev.split()
monogram = ""

for szo in szavak:
    if szo.lower().startswith("dzs"):
        monogram += "DZS"
    elif szo.lower().startswith(("cs","gy","ly","ny","sz","ty","zs")):
        monogram += szo[:2].upper()
    else:
        monogram += szo[0].upper()

print("Monogram:", monogram)

#Varga Gyula, Pádár Zsombor, Szilágyi Ákos
