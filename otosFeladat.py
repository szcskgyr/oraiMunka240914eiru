# 5. feladat
# Tárolj el két számot egy-egy változóba!
# Írd ki az összegüket, különbségüket, szorzatukat és hányadosukat, hatványukat!

import beolvas

szam1 = beolvas.tortSzamBeolvas()
szam2 = beolvas.tortSzamBeolvas()

# print("A számok:\n")
# print("összege:", szam1+szam2)
# print("különbsége:", szam1-szam2)
# print("szorzata:", szam1*szam2)
# print("hányadosa:", szam1/szam2)
# print("hatványa:", szam1**szam2)

# műveletek
osszeg = szam1+szam2
kulonbseg = szam1-szam2
szorzat = szam1*szam2
hanyados = szam1/szam2
maradek = szam1 % szam2
hatvany = szam1**szam2

# kiírás
print(osszeg)
print(kulonbseg)
print(szorzat)
print(hanyados)
print(maradek)
print(hatvany)
