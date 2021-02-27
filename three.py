class Address:

    town = ""
    street = ""
    house = ""
    flat = 0
    index = 0

    def __init__(self, town, street, house, flat, index):
        self.town = town
        self.street = street
        self.house = house
        if not(0 < flat < 1000):
            raise Exception("Wrong flat number!")
        self.flat = flat
        if not (100000 <= index < 1000000):
            raise Exception("Wrong index!")
        self.index = index

    def __eq__(self, other):
        return self.town == other.town and self.street == other.street and self.flat == other.flat and self.house == other.house and self.index == other.index

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.index > other.index

    def __lt__(self, other):
        return self.index < other.index


ad1 = Address("Moscow", "Arbat", "№1", 20, 100000)
ad2 = Address("Saint-Petersburg", "Sadovaya", "№132", 56, 150000)
print(ad1 != ad2)
print(ad1 > ad2)
try:
    Address("N", "N", "1", 1, 1000000)
except Exception as e:
    print(e)
