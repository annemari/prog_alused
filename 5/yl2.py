fail = open("konto.txt", encoding="UTF-8")
vastuvõetud = []
for rida in fail:
     vastuvõetud.append(float(rida))
fail.close()
print(vastuvõetud[:]+"\n")