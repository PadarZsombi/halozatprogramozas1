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
