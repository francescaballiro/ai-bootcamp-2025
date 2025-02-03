class Directory:
    def __init__(self):
        self.contacs = []

    def add(self, person):
        self.contacs.append(person)

    def __len__(self):
        return len(self.contacs)

    def query(self, name):
        return [person for person in self.contacs if person.name == name or person.surname == name]

    def find(self, cerca_termini):
        risultato = []
        for person in self.contacs:
            if person.name == cerca_termini:
                risultato.append(person)
            elif person.surname == cerca_termini:
                risultato.append(person)
            elif person.phone is not None and cerca_termini in person.phone:
                risultato.append(person)
        return risultato


class Person:
    def __init__(self, name, surname, phone=None):
        self.name = name
        self.surname = surname
        self.phone = phone

class Business:
    def __init__(self, name=None, phone=None):
        self.name = name
        self.phone = phone
        self.surname = None



directory = Directory()
assert len(directory) == 0
directory.add(Person(name="Margaret", surname="Hamilton", phone="01-234-567"))
directory.add(Business(name="Vedrai", phone="+39-333-333333"))
directory.add(Person(name="Linda", surname="Hamilton"))
assert len(directory) == 3
assert [el.phone for el in directory.query(name="Vedrai")] == ["+39-333-333333"]
assert [el.phone for el in directory.query(name="Margaret")] == ["01-234-567"]
assert [el.phone for el in directory.find("Hamilton")] == ["01-234-567", None]
assert [el.name for el in directory.find("333")] == ["Vedrai"]