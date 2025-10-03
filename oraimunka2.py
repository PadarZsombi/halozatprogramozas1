nev = input("Add meg a teljes neved: ")
szavak = nev.split()
monogram = ""

for szo in szavak:
    szo_lower = szo.lower()
    
    if len(szo_lower) >= 3 and szo_lower[0] == 'd' and szo_lower[1] == 'z' and szo_lower[2] == 's':
        monogram += "Dzs"
    
    elif len(szo_lower) >= 2 and (
        (szo_lower[0] == 'c' and szo_lower[1] == 's') or
        (szo_lower[0] == 'g' and szo_lower[1] == 'y') or
        (szo_lower[0] == 'l' and szo_lower[1] == 'y') or
        (szo_lower[0] == 'n' and szo_lower[1] == 'y') or
        (szo_lower[0] == 's' and szo_lower[1] == 'z') or
        (szo_lower[0] == 't' and szo_lower[1] == 'y') or
        (szo_lower[0] == 'z' and szo_lower[1] == 's')
    ):
        monogram += szo[0].upper() + szo[1].lower()
    else:
        monogram += szo[0].upper()

print("Monogram:", monogram)
