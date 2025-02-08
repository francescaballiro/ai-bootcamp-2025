import sqlite3
import csv
import random
from datetime import datetime, timedelta


conn = sqlite3.connect('students.db')  # Sostituisci con il percorso del tuo database
cursor = conn.cursor()

# Esegui la query per ottenere gli ID dalla tabella
cursor.execute("SELECT id FROM students")  # Modifica "studenti" con il nome della tua tabella
student_ids = cursor.fetchall()  # Ottieni tutti gli ID

with open("studenti_assignments.csv", mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["id", "data_assignment", "hours_absence"])  # Scrivi l'intestazione

    # Definisci l'intervallo di date (date randomiche)
    start_date = datetime(2020, 1, 1)  # Inizio dell'intervallo
    end_date = datetime(2025, 12, 31)  # Fine dell'intervallo
    delta = end_date - start_date


    # Esegui la scrittura per ogni studente
    for student_id in student_ids:
        # Genera una data casuale per ogni studente
        random_days = random.randint(0, delta.days)
        random_date = start_date + timedelta(days=random_days)

        # Scrivi i dati nel file CSV
        writer.writerow([student_id[0], random_date.strftime("%Y-%m-%d"), random.randint(0, 10)])


cursor.execute("SELECT id,first_name,last_name,year_of_birth,gender,email FROM students")  # Modifica "studenti" con il nome della tua tabella
students = cursor.fetchall()

with open('students_no_assignments.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["id", "first_name", "last_name", "year_of_birth", "gender", "email"])
    writer.writerows(students)

conn.close()


with open ('students_no_assignments.csv', 'r') as fd:
    reader = csv.reader(fd, delimiter=';')
    studenti_no_assigments = []
    for l in reader:
        studenti_no_assigments.append(l)
    studenti_no_ass = studenti_no_assigments[1:]


with open ("studenti_assignments.csv", 'r') as fd:
    reader = csv.reader(fd, delimiter=';')
    studenti_assignments = []
    for l in reader:
        studenti_assignments.append(l)
    studenti_ass = studenti_assignments[1:]

connessione = sqlite3.connect("assignments.db")
cursor = connessione.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students_no_assignments (
id INTEGER PRIMARY KEY ,
first_name TEXT,
last_name TEXT,
year_of_birth INTEGER,
gender TEXT,
email TEXT)
 ''');

cursor.execute('''
CREATE TABLE IF NOT EXISTS studenti_assignments (
id INTEGER,
data_assignment TEXT,
hours_absence INTEGER DEFAULT 0) 
 ''');
connessione.commit()

cursor.execute('DELETE FROM students_no_assignments')
cursor.execute('DELETE FROM studenti_assignments')
connessione.commit()

cursor.executemany(
    "INSERT OR REPLACE INTO students_no_assignments (id, first_name, last_name, year_of_birth, gender, email) VALUES (?, ?, ?, ?, ?, ?) ON CONFLICT DO NOTHING",
    studenti_no_ass)
connessione.commit()

cursor.executemany(
    "INSERT OR REPLACE INTO studenti_assignments (id, data_assignment, hours_absence) VALUES (?, ?, ?) ON CONFLICT DO NOTHING",
    studenti_ass)
connessione.commit()

#l'id, l'anno di nascita e le date di consegna degli studenti nati dopo il 2000
cursor.execute('''
    SELECT s.id, s.year_of_birth, sa.data_assignment
    FROM students_no_assignments s
    JOIN studenti_assignments sa ON s.id = sa.id
    WHERE s.year_of_birth = 2000
''')
results = cursor.fetchall()
print("ecco l'id, l'anno di nascita e le date di consegna degli studenti nati dopo il 2000")
print(results)

#COGNOME E ORE DI ASSENZA DELLA STUDENTESSA DI NOME JANE CON MENO ORE DI ASSENZA
cursor.execute('''
SELECT s.last_name, s.first_name, sa.hours_absence
FROM students_no_assignments s
JOIN studenti_assignments sa ON s.id = sa.id
WHERE s.first_name = 'Jane' 
ORDER BY sa.hours_absence ASC
LIMIT 1;''')

results = cursor.fetchall()
print("COGNOME E ORE DI ASSENZA DELLA STUDENTESSA DI NOME JANE CON MENO ORE DI ASSENZA")
print(results)

#lista in ordine di consegna degli studenti
cursor.execute('''
SELECT s.last_name, s.first_name, s.gender, sa.data_assignment
FROM  students_no_assignments s
JOIN studenti_assignments sa ON s.id = sa.id
ORDER BY sa.data_assignment ASC;''')

results = cursor.fetchall()
print("lista in ordine di consegna degli studenti")
for result in results:
    print(result)
# Chiudi la connessione
connessione.close()
