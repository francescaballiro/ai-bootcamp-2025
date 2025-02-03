import csv

#apro il file e ordino in base al cognome indicizzando e salvando in un file
with open("data.csv") as fd:
    reader = csv.reader(fd)
    # legge l'intestazione
    intestazione = next(reader)
    # si convertono le righe in una lista
    lines = list(reader)
    # ordino le righe in base al cognome
    lines.sort(key=lambda line: line[1])
    # stampo l'intestazione
    print(intestazione)

    contatore = 1
    for line in lines:
        print(f"{contatore}: {line}")
        contatore += 1

#apro il file e ordino in base al nome
with open("data.csv") as fd:
    reader = csv.reader(fd)
    intestazione = next(reader)
    lines1 = list(reader)
    lines1.sort(key=lambda el: el[0])
    print(intestazione)
    for el in lines1:
        print(el)

with open("data2.csv", mode='w', newline='') as fd2:
    writer = csv.writer(fd2)
    writer.writerow(intestazione)
    writer.writerows(lines)
