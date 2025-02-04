import csv

#apro il file e ordino in base al cognome
with open("data.csv") as fd:
    reader = csv.reader(fd)
    intestazione = next(reader)
    def f(cognomi):
        return cognomi[1]
    lines= list(sorted(reader, key=f))

    contatore = 1
    for line in lines:
        print(f"{contatore}: {line}")
        contatore += 1

#apro il file e ordino in base al nome
with open("data.csv") as fd:
    reader = csv.reader(fd)
    intestazione = next(reader)
    def n(nomi):
        return nomi[0]
    lines1 = list(sorted(reader, key=n))
    print(intestazione)
    for el in lines1:
        print(el)

with open("data2.csv", mode='w', newline='') as fd2:
    writer = csv.writer(fd2)
    writer.writerow(intestazione)
    writer.writerows(lines)

