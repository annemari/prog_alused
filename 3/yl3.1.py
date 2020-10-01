#Üldtsükkel
for kord in range(1, 5, 1):
    print(str(kord) + ". tere")
    print("===================================")
    
    #vastupidi
    for kord in range(1, 5, -1):
        print(str(kord) + ". tere")

    print("===================================")
    kord = 1
    while(kord <= 5):
        print(str(kord) + ". tere")
        kord = kord + 1 #kord += 1