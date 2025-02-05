import sqlite3
import csv

with open ("students.csv" , 'r') as fd:
    reader = csv.reader(fd, delimiter=';')
    studenti1 = []
    for line in reader:
        #print(line)
        studenti1.append(line)

studenti = studenti1[1:]
#print(studenti)

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS students (
id INTEGER PRIMARY KEY ,
first_name TEXT,
last_name TEXT,
year_of_birth INTEGER,
gender TEXT,
email TEXT,
assignments DEFAULT 0) ''');
conn.commit()

cur.executemany(
    "INSERT INTO students (id, first_name, last_name, year_of_birth, gender, email, assignments) VALUES (?, ?, ?, ?, ?, ?, ?) ON CONFLICT DO NOTHING",
    studenti)
conn.commit()

cur.execute("SELECT * FROM students WHERE year_of_birth = 2000")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.execute("SELECT first_name, last_name, assignments FROM students WHERE assignments = (SELECT MAX(assignments) FROM students)")
rows = cur.fetchall()
print("The student with the highest number of assignments is:")
for row in rows:
    print(row)

cur.execute("SELECT first_name, last_name  FROM students ORDER BY assignments DESC")
rows = cur.fetchall()
print("This is a ranking of students by number of assignments: ")
for row in rows:
    print(row)
