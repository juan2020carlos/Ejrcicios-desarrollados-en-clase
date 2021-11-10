class Location:
    def __init__(self, name, country):
        self.name = name
        self.country = country
    
    def MyLocation (self):
        print("Hi, mi nombre es " + self.name + " y vivo en " + self.country + ".")


loc = Location("Tomas", "Portugal")
loc.MyLocation()

loc2 = Location("Ying", "China")
loc3 = Location("Amare", "Kenya")
loc2.MyLocation()
loc3.MyLocation()

your_lock = Location("Juan", "Perú")
your_lock.MyLocation()