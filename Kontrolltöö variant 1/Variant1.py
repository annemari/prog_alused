#Funktsioon Inimeste_arv

#Küsib kasutajalt turniiril osalevate naiskondade arvu
#naiskonnad = int(input("Sisestage turniiril osalevate naiskondade arv: "))
#Küsib kasutajalt tugiisikute arvu
#tugiisikud = int(input("Sisestage tugiisikute arv: "))
#Valem
#inimeste_arv = naiskonnad*(22+tugiisikud)
#Väljastab inimeste arvu
#print ("Turniiril osalevate inimeste arv on " + str(inimeste_arv))


#Programm

import random

#Küsib kasutajalt toimumiskoha
toimumiskoht = input("Kus toimusid maailmameistrivõistlused: ")
print("Turniirid toimusid "+toimumiskoht)
turniiridkok = int(input("Kui palju turniire toimus: "))

def inimeste_arv(x, y):
    isikudkok = x * (22 + y)
    return isikudkok

x = turniiridkok
kõikinimkokku = 0

#Genereerib juhusliku arvu ja rakendab tugiisikute valemit
while x > 0:
    naiskonna_arv = random.randint(10,30)

    if naiskonna_arv < 15:
        tugiisik = 10
    else:
        tugiisik = 8

    #Arvutab kokku inimesed naiskondades pluss tugiisikud. Igal turniiril eraldi
    inimesed = inimeste_arv(naiskonna_arv,tugiisik)
    kõikinimkokku += inimesed

    print("Turniiril oli "+str(naiskonna_arv)+" naiskonda ja vastavalt inimesi - "+str(inimesed))
    x -= 1

#Väljastab kogu turniiril osalevate inimeste arvu
print("Kokku oli kõigil turniiridel inimesi: "+str(kõikinimkokku))
