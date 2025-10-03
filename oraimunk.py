nev = input("Add meg a teljes neved: ")
szavak = nev.split()
monogram = ""

for szo in szavak:
    szo_lower = szo.lower()
    
    if szo_lower.startswith("dzs"):
        monogram += "Dzs"
    elif szo_lower.startswith(("cs", "gy", "ly", "ny", "sz", "ty", "zs")):
        monogram += szo[:2].capitalize()
    else:
        monogram += szo[0].upper()

print("Monogram:", monogram)
<<<<<<< HEAD
=======

#Varga Gyula, Pádár Zsombor, Szilágyi Ákos
>>>>>>> 6e3b7abd6e616883b03d7d9ddf67fbda179c64d6
