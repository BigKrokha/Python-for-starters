from random import randint

listik = []
listik.append(randint(0,100))

while len(listik) < 20:
    toadd = randint(0,100)
    fl = True
    for x in listik:
        if x == toadd:
            fl = False
    if fl: listik.append(toadd)


print(listik)

#[16, 24, 60, 68, 76, 59, 93, 26, 28, 73, 4, 8, 61, 12, 90, 78, 98, 40, 14, 29]