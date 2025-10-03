# A róka libát lop a faluból, a hét minden napján egyet. Ezek súlyát tároltuk el a libak.txt-ben. A farkas várja a falu határában a rókát és a 3 kg-nál nehezebb libát elveszi, a kisebbeket meghagyja a rókánál.

# 0. Beolvasás
libak = []
with open("libak.txt") as fin:
    for suly in fin:
        libak.append(int(suly.strip()))
print(libak)

# 1. Hány kiló libát evett a róka a héten?
roka_kilo = 0

for liba in libak:
    if liba <= 3:
        roka_kilo = roka_kilo + liba
print(f"{roka_kilo} kg libát evett a róka a héten.")

# 2. Átlagosan hány kilósak a rókánál maradt libák?
roka_darab = 0
for liba in libak:
    if liba <= 3:
        roka_darab += 1
print(f"Átlagosan {roka_kilo/roka_darab} kilósak a rókánál maradt libák")
    
# 3. Előfordult-e, hogy a róka legalább 3kg-os libát lopott?
volt_legalabb_harom = False
for liba in libak:
    if liba >= 3:
        volt_legalabb_harom = True

if volt_legalabb_harom:
    print("Előfordult, hogy a róka legalább 3kg-os libát lopott.")
else:
    print("Nem fordult elő.")
        
# 4. Előfordult-e, hogy a róka kisebb libát lopott, mint az előző napon?
# 5. Hányadik napon sikerült először 3kg-nál nehezebb libát lopni?
# 6. Volt-e 6kg súlyú liba, ha volt akkor melyik napon?
# 7. Hány liba jutott a héten a farkasnak?
# 8. Hány kilós volt a rókánál maradó legnagyobb libának?