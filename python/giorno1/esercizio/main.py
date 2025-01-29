print("Inizio programma")

# Assegno la variabile foo
foo = False

# Questi controlli assert devono passare tutti
assert bool(1)
assert False == False
assert True is True
assert True != False
assert None is not False

# Faccio alcune operazioni aritmetiche sui numeri interi
bar = 0
baz = 1
result = bar / baz

# Incremento il risultato di uno

result += 1

# Decremento il risultato di uno

result -= 1

# Controllo che il valore non sia negativo
assert result >= 0

# Concateno le stringhe
message = "hello" + "world"

# Creo una lista e la estendo
li1 = [1, 2]
li1 += [3]

# Non mi ricordo come si "prepende" un valore...
li1.insert(0, 0)

# Verifico che il risultato sia quello che mi aspetto
assert li1 == [0, 1, 2, 3]

# Creo una tupla e la estendo
tu1 = (1, 2)
tu1 += (3,)

assert tu1 == (1, 2, 3)

# Creo un dict

d1 = {}
d1["a"] = 1
d1["b"] = 2

assert d1["a"] == 1
assert d1 == {"a": 1, "b": 2}

# Cancello la chiave "b"
del d1["b"]

# Controllo che il dict non contenga ancora la chiave "b"
assert "b" not in d1

# Potrei anche controllarlo in questo modo
# e verificare anche la presenza di "a"
if "b" not in d1:
    assert True
elif "a":
    assert False
else:
    assert True

# Stampo la scritta "Ciao" tre volte poi esco
# Conto le volte che l'ho stampata
count = 0
for idx in [0, 1, 2]:
    count += 1
    print("Ciao")

# Controllo che l'abbia stampata tre volte
assert count == 3

# Stampo di nuovo la scritta "Ciao" tre volte poi esco
num = 3
while num > 0:
    print("Ciao")
    num -=1

print("Fine programma")