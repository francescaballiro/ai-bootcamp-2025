class Country:
    def __init__(self, name):
        self.name = name
        self._regions = []

    def add(self, region):
        self._regions.append(region)

    @property
    def pop(self):
        return sum(region.pop for region in self.regions)

    @property
    def most(self):
        all_cities = [city for region in self.regions for city in region.cities]
        return max(all_cities)


class Region():
    def __init__(self, name):
        self.name = name
        self._cities = []

    def add(self, city):
        self._cities.append(city)

    @property
    def pop(self):
        return sum(city.pop for city in self._cities)


class City():
    def __init__(self, city, pop):
        self.city = city
        self.pop = pop


italy = Country("Italy")
assert italy.name == "Italy"
sicily = Region("Sicily")
italy.add(sicily)
sicily.add(City("Catania", pop=300_000))
sicily.add(City("Palermo", pop=600_000))
assert sicily.pop == 900_000