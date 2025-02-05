import random
import csv
from datetime import datetime


def gioca():
    numero_random = random.randint(1, 100)
    tentativi = 0

    inizio_partita = datetime.now()

    while True:
        try:
            numero_inserito = int(input("Inserisci un numero da 1 a 100 da indovinare>> "))
            tentativi += 1
            if 1 <= numero_inserito <= 100:
                if numero_inserito == numero_random:
                    print(f"Hai indovinato al {tentativi}, congratulazioni")
                    nome = input("inserisci il tuo nome : ").capitalize()
                    fine_partita = datetime.now()
                    durata = (fine_partita - inizio_partita).total_seconds()
                    data_e_ora= fine_partita.strftime("%x-%X")
                    lista.append([nome , f"{tentativi}" , data_e_ora, durata ])
                    print(f"Hai indovinato al {tentativi} ° tentativo")
                    break
                elif numero_inserito > numero_random:
                    print("Il numero è troppo alto! Ritenta")
                elif numero_inserito < numero_random:
                    print("Il numero è troppo basso! Ritenta")
                else:
                    print("Ehi, ricordati di inserire un numero da 1 a 100!")

        except ValueError:
            print("Input non valido, per favore inserisci un numero!")
            continue

lista = []

while True:
    gioca()
    risposta = input("Vuoi continuare a giocare? (s/n): ").lower()
    if risposta != 's':
        print("E' stato un piacere giocare con te! Arrivederci!")
        break

lista.sort(key=lambda x: int(x[1]))

with open("lista.cvs", mode='w', newline='') as fd:
    writer = csv.writer(fd)
    writer.writerow(["Nome", "Tentativi", "Data e Ora", "Durata in secondi"])
    writer.writerows(lista)

print("Punteggi salvati")
