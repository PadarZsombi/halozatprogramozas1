lista = [2,4,1,8,3]

# A.1 lista elemeinek összege
osszeg = 0
for szam in lista:
    osszeg += szam

print(f"A.1 lista elemeinek összege: {osszeg}")
print(f"A.1 lista elemeinek összege: {sum(lista)}")

#B.1 lista elemeinek darabszama

darab = 0
for _ in lista:
    darab += 1

print(f"B.1 lista elemeinek darabszama: {darab}")
print(f"B.1 lista elemeinek darabszama: {len(lista)}")

#A.2 paros szamok atlaga
paros_osszeg = 0
paros_darab = 0

for szam in lista:
    if szam % 2 == 0:
        paros_osszeg += szam
        paros_darab += 1

print(f"A.2 paros szamok atlaga: {paros_osszeg / paros_darab:.3f}")


#B.2 paros szamok darab szama
print(f"B.2 paros szamok darab szama: { paros_darab}")

#A.2 es B.2 

parosok_lista = [szam for szam in lista if szam % 2 == 0]
#parosok lista = [2,4,8]
print(f"A.2 paros szamok atlaga: {sum(parosok_lista) / len(parosok_lista):.2f}")
print(f"B.2 paros szamok darab szama: {len(parosok_lista)}")


#AB.3 jelenitsd meg savdiagrammon a listat
for szam in lista:
    print(szam, "*" * szam)
    
