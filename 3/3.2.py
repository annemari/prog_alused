ringide_arv = int(input("Sisesta ringide arv: "))
ringi_number = 1
porgandite_arv = 0
while(ringi_number <= ringide_arv):
    print(ringi_number)
    if(ringi_number % 2 == 0):
        porgandite_arv = porgandite_arv + ringi_number
        print("Said " + str(ringi_number) + " porgandit")
        print("kokku hetkel on " + str(porgandite_arv) + " porgandit")
    ringi_number  += 1

print("Porgandite koguaev " + str(porgandite_arv))