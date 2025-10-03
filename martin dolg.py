# list = [1,4,5,6,8,3]

# osszeg = 0

# for szam in list:
#     osszeg = osszeg + szam

# print(f"A számok összege:{osszeg}")

# db = 0

# for szam in list:
#     db = db+1
# print(f"{db}")


# p_szamok = []

# for szam in list:
#     if szam % 2 == 0:
#         p_szamok.append(szam)
# print(f"A páros számok:{p_szamok}")

# paratlan_db = 0

# for szam in list:
#     if szam % 2 > 0:
#         paratlan_db = paratlan_db + 1
# print(f"A páratlan számok összege: {paratlan_db}")

nevek = []

while True:
    k_nev = input(f"Kérek egy Keresztnevet: ")
    if  k_nev in nevek:
        break
    nevek.append(k_nev)
print(nevek)    

