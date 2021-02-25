# This is the completely abstract mainimport code that needs to be overwritten when inheriting


class mainImport():

    def __init__(self):
        self.locations = []

    def checkIn(self, name):
        for loc in self.locations:
            if name == loc.name:
                return loc
        return None

    # This needs to be changed per region
    def createLocation(self, name):
        print("Using the wrong main import")
        return None

    # This should be ok
    def getLocation(self, name):
        loc = self.checkIn(name)

        if loc is None:
            loc = self.createLocation(name)
            self.locations.append(loc)

        return loc
