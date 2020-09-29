Pnimi = input("Sisestage Leedu perekonnanimi: ")

if Pnimi[-2:] == "ne":
    print("Abielus")
elif Pnimi[-2:] == "te":
    print("Vallaline")
elif Pnimi[-1] == "e" and Pnimi[-2:] != "ne" and Pnimi[-2:] != "te":
    print("Määramata")
elif Pnimi[-1] != "e":
    print("Pole ilmselt leedulanna perekonnanimi")