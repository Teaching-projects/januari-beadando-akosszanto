import random

#Blackjack tét nélkül, ezáltal nincsen benne surrender, split és double.

'''
A játék szabályai:

- A játék első szakaszában két lapot oszt az osztó neked és saját magának, amiből ő eggyet megmutat.
- A játékos az osztás követően bármennyi lapot kérhet ameddig el nem éri a 21 értéket, ha pont megáll a 21-en ő nyert, ha túllépi veszít.
- Az osztó az osztást követően húz saját magának mint addig amíg el nem éri  17 értéket.
- Az nyer aki közelebb van a 21-hez, vagy 21-e van, vagy peddig ha valaki túl haladta a 21-et.
'''

def laphuz1():
    lap_ertekek = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    a1 = random.choice(lap_ertekek)
    return a1

def laphuz2():
    lap_ertekek_asz = [2, 3, 4, 5, 6, 7, 8, 9, 10] 

    a2 = random.choice(lap_ertekek_asz)
    return a2

def laphuzoszto1():
    lap_ertekek = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    b1 = random.choice(lap_ertekek)
    return b1

def laphuzoszto2():
    lap_ertekek_asz = [2, 3, 4, 5, 6, 7, 8, 9, 10] 

    b2 = random.choice(lap_ertekek_asz)
    return b2

#lap_ertekek = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#lap_ertekek_asz = [2, 3, 4, 5, 6, 7, 8, 9, 10]

sajat_kartyak = 0
oszto_kartyak = 0

#a1 = random.choice(lap_ertekek)
#a2 = random.choice(lap_ertekek_asz)

#b1 = random.choice(lap_ertekek)
#b2 = random.choice(lap_ertekek_asz)

a1 = laphuz1()
a2 = laphuz2()

b1 = laphuzoszto1()
b2 = laphuzoszto2()

sajat_kartyak = sajat_kartyak + a1
print("Kaptál egy", a1, "értékű lapot.")
print("Lapjaid értéke összesen:", sajat_kartyak)

print(" ")

sajat_kartyak = sajat_kartyak + a2
print("Kaptál egy", a2, "értékű lapot.")
print("Lapjaid értéke összesen:", sajat_kartyak)

print(" ")

oszto_kartyak = oszto_kartyak + b1
print("Osztó első lap értéke:", b1)
print("Osztó lapjainak összege:", oszto_kartyak)

print(" ")

if sajat_kartyak == 21:
    print("Blackjacked van!")
    exit()

kerdes = input("Szeretnél lapot húzni ? Igen vagy Nem ?")
kerdes = str(kerdes)

while kerdes == 'Igen' or kerdes == "igen":
    uj_lap = laphuz1()
    if uj_lap == 11 and sajat_kartyak > 10:
        sajat_kartyak += 2
        uj_lap = 2
    else:
        sajat_kartyak = sajat_kartyak + uj_lap
    print(" ")
    print("Kaptál egy", uj_lap , "értékű lapot.")
    print("Lapjaid értéke összesen:", sajat_kartyak)
    print(" ")
    if sajat_kartyak == 21:
        print("Blackjacked van!")
        exit()
    elif sajat_kartyak > 21:
        print("Vesztettél! Meghaladtad a 21-et!")
        exit()  
    kerdes = input("Szeretnél lapot húzni ? Igen vagy Nem ?")

oszto_kartyak = oszto_kartyak + b2
print("Az osztó második lapja:", b2)
print("Osztó lapjainak összege:", oszto_kartyak)


uj_lap_oszto = laphuz1()
if oszto_kartyak == 21:
    print(" ")
    print("Osztó következő lapjának értéke:", uj_lap_oszto)
    print("Osztó lapjainak összege: ", oszto_kartyak)
    print(" ")
    print("Vesztettél! Az osztónak Blackjackje van!")
    exit()
while oszto_kartyak <= 16:
    uj_lap_oszto = laphuz1()
    if uj_lap_oszto == 11 and oszto_kartyak > 10:
        oszto_kartyak += 2
        uj_lap_oszto = 2
    else:
        oszto_kartyak = oszto_kartyak + uj_lap_oszto
    if oszto_kartyak == 21:
        print(" ")
        print("Osztó következő lapjának értéke:", uj_lap_oszto)
        print("Osztó lapjainak összege: ", oszto_kartyak)
        print(" ")
        print("Vesztettél! Az osztónak Blackjackje van!")
        exit()
    print(" ")
    print("Osztó következő lapjának értéke:", uj_lap_oszto)
    print("Osztó lapjainak összege: ", oszto_kartyak)
    print(" ")

if oszto_kartyak > 21:
    print("Nyertél! Az osztó meghaladta a 21-et!")
    exit()
if oszto_kartyak < 21 and oszto_kartyak > sajat_kartyak:
    print("Vesztettél! Az osztónak nagyobb lapjai vannak!")
    exit()
elif sajat_kartyak < 21 and sajat_kartyak > oszto_kartyak:
    print("Nyertél! A Lapjaid értéke nagyobb mint az osztóé!")
    exit()