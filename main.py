papka1 = open("1.txt")
papka2 = open("2.txt")
novoe3 = open("3.txt", "w")
spisok1 = []
spisok2 = []
for i in papka1:
    spisok1.append(i.strip( ))
for j in papka2:
    spisok2.append(j.strip( ))
if len(spisok1) > len(spisok2):
    novoe3.write(papka2.name + "\n")
    novoe3.write(str(len(spisok2)) + "\n")
    for k in spisok2:
        novoe3.write(k + "\n")
    novoe3.write(papka1.name + "\n")
    novoe3.write(str(len(spisok1)) + "\n")
    for n in spisok1:
        novoe3.write(n + "\n")
else:
    novoe3.write(papka1.name + "\n")
    novoe3.write(str(len(spisok1)) + "\n")
    for n in spisok1:
        novoe3.write(n + "\n")
    novoe3.write(papka2.name + "\n")
    novoe3.write(str(len(spisok2)) + "\n")
    for k in spisok2:
        novoe3.write(k + "\n")
    