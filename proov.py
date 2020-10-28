import random #impordin funktsiooni random

#Küsin kasutaja käest toimumiskoha ja turniiride arvu
finaalkoht = input("Kus toimusid maailmameistrivõistlused: ")
print("Turniirid toimusid "+finaalkoht)
turniiridkok = int(input("Kui palju turniiri toimus: "))

def inimeste_arv(x, y):
    isikudkok = x * (22 + y)
    return isikudkok

x = turniiridkok
kõikinimkokku = 0

while x > 0:
    naiskonnaarv = random.randint(10,30) #Genereerib juhusliku arvu 10-30
    #Valib tugiisikute arvu vastavalt naiskonnaarvule kui on 10 siis on tugiisikuid 3 <kui 15 siis 10 ja ülejäänud on 10 tugiisikut
    if naiskonnaarv == 10:
        tugiisik = 3
    elif naiskonnaarv < 15:
        tugiisik = 10
    else:
        tugiisik = 8
    #Funktsioon inimeste_arv(x,y) võtab parameetrid naiskonnaarv ja tugiisik, millega väljastab vastava inimeste arvu turniiril
    vastavini = inimeste_arv(naiskonnaarv,tugiisik)
    #kõikinimkokku salvestatakse kõikide turniiridel olevad inimeste arvud kokku
    kõikinimkokku += vastavini

    print("Turniiril oli "+str(naiskonnaarv)+" naiskondi ja vastavalt inimesi: "+str(vastavini))
    x -= 1

#Väljastab kogu turniiril osalevate inimeste arvu
print("Kokku oli kõigil turniiridel inimesi: "+str(kõikinimkokku))
