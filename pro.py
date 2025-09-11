from os import sep


print("Szia", end=" ")
print("Tibi")
print("Szia", "Tóth", "Karcsi", "!", sep="")
print("Szia Tóth Karcsi!")
nev = "Tóth Karcsi"
print(f"Szia {nev}!")
print("Szia", "Peti", sep="\n", end="!") #\t
#adattípusok
# int()
# float()
# str()
# bool()
# list()
# set()
print()
print(int("5"))
print(float(5))
print(type(str(5.0)))
print(bool(-1))
print(["hétfő", "kedd", "szerda"])
napok = ["hétfő", "kedd", "szerda"]
print(f"Napok: {napok}")
nevek = ["Tibi", "Sanyi", "Tibi"]
print(f"Nevek: {set(nevek)}")
print(tuple([1,2,3]))


# HF: git parancsok:
# git init: Adott mappa verziókövetésének indítása
# git add: Hozzáadja a módosított fájlokat a következő commit-hoz
# git clone: Letölti egy távoli repó másolatát a helyi eszközre
# git config --global user.name: Beállítja a Git felhasználónevét
# git config --global user.email: Beállítja a Git email-címét
# git log: Megmutatja a commit-elési előzményeket
# git commit -m: Elmenti a változásokat a Git tárolóba egy megadott üzenettel
# git push: Feltölti a commit-okat a távoli repóba
