print("Sisestage ainepunktide arv")
ainepunktid = int(input())
print("Sisestage nädalate arv")
nadalateArv = int(input())
aineAjakulu = int(ainepunktid)**26
print(aineAjakulu)
nadal = int(nadalateArv)**10
nadalaAjakulu = int(nadal)/int(aineAjakulu)
print(nadalaAjakulu)
