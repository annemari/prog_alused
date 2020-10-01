
from random import randint
soovitud_kord = int(input("Sisesta visete arv: "))
kord = 1
while(kord <= soovitud_kord):

    taring = randint(1, 6)
    print(taring)
    kord += 1