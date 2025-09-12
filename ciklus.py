#ciklusok

# lista = [1, 2, 3, 4, 5]


# def osszegez(lista):
#     osszeg = 0
#     for elem in lista:
#         osszeg += elem
#     return osszeg

# def paros_szamok_darabszama(lista):
#     db = 0
#     for szam in lista:
#         if szam % 2 == 0:
#             db+=1
#     return db


# print(f"A lista elemeinek összege: {osszegez(lista)}")

# print(f"A lista páros elemeinek darabszáma: {paros_szamok_darabszama(lista)}")

# # Írass ki egy sorba 5 *-ot
# print("*"*5)

# for i in range(5):
#     print("*", end="")
# print()

# Rajzolj piramist
#     *
#    ***
#   ***** 
#  *******
# *********

n = 9
space_db = n - 1
csillag_db = 1
for i in range(n):
    print(" " * space_db, end="")
    print("*" * csillag_db)
    space_db -= 1
    csillag_db += 2


for i in range(1, 11):
    for j in [1,2,3,4,5,6,7,8,9,10]:
        print(f"{i*j:4}", end = "")
    print()