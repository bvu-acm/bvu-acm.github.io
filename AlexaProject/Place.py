# Already in its basic abstract form

class Place:
    def __init__(self, person):
        self.name = "place"  # Here is where the name of your place goes. String
        self.description = "blah"  # This is the description of the place. String
        self.connections = []  # This holds the name of the places that you can go from here
        self.comline = person.comline
        self.items = []  # This holds just the names of the items you want to be in the location. [String]
        self.npcs = []  # This holds a list of the npcs name. Works like items except they can be
        # grabbed from either the main folder of basic npcs or specific ones made for that region

# Note: The default values can be changed later I just put them there for testing purposes
