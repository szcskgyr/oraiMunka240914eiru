# 11. Adott két pozitív szám, melyek 50 és 150 közöttiek.
# Írd ki a két változót a nevükkel és értékükkel együtt,
# majd cseréld meg a tartalmukat és újra írasd ki őket!

import random

szam1 = random.randint(50,150)
szam2 = random.randint(50,150)

print("szam1="+str(szam1), "szam2="+str(szam2))

# csere1

atmenet = szam1
szam1 = szam2
szam2 = atmenet

print("szam1="+str(szam1), "szam2="+str(szam2))

# csere2

atmenet = szam2
szam2 = szam1
szam1 = atmenet

print("szam1="+str(szam1), "szam2="+str(szam2))
