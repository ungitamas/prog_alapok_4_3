# 4/3.	A mellékelt paszuly.txt szövegfájban az Égig érő paszuly című mese olvasható. Olvassa be a szövegfájlt tartalmát egy erre alkalmas adatszerkezetbe, majd oldja meg az alábbi feladatokat:
# a.	Írja ki a képernyőre, hány sort olvasott be a fájlból!
# b.	Írja ki, hogy a mese hány mondatból áll! (Minden mondat végén pont, kérdőjel vagy felkiáltójel található.)
# c.	Hányféle ragozott formában fordul elő a paszuly szó a szövegben? Gyűjtse össze és írja ki az összes ragozott formát! Ügyeljen arra, hogy egy szót csak egyszer jelenítsen meg és a szavak ne tartalmazzák az őket követő írásjeleket (; , . ! ?)
# d.	Írja ki, melyik a legrövidebb sor a fájlban (melyik sor tartalmazza a legkevesebb karaktert)! Jelenítse meg magát a sort és karaktereinek számát is!

mese = []

with open("paszuly.txt" ,"r", encoding="utf-8") as bemenet: 
    for sor in bemenet:
        mese.append(sor.strip())

print(f"{len(mese)} sort olvastunk be a fájlból") 

mondat = 0
for sor in mese: 
    mondat += sor.count(".")+sor.count("?")+sor.count("!")

print(f"A mese {mondat} mondatból áll")