# 6. Tárolj el két számot egy-egy változóba!
# Írd ki az összegüket, különbségüket, szorzatukat és hányadosukat, hatványukat teljes műveleti sorrendben.

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
hatvany1 = szam1**szam2
hatvany2 = szam2**szam1

# kiírás
print(str(szam1)+"+"+str(szam2)+"="+str(osszeg))
print(str(szam1)+"-"+str(szam2)+"="+str(kulonbseg))
print(str(szam1)+"*"+str(szam2)+"="+str(szorzat))
print(str(szam1)+"/"+str(szam2)+"="+str(hanyados))
print(str(szam1)+"%"+str(szam2)+"="+str(maradek))
print(str(szam1)+"^"+str(szam2)+"="+str(hatvany1))
print(str(szam2)+"^"+str(szam1)+"="+str(hatvany2))
