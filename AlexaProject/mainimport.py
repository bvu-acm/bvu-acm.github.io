# This is the completely abstract mainimport code that needs to be overwritten when inheriting


class mainImport():

    def __init__(self):
        self.locations = []
        self.npcs = []

    def checkIn(self, name):
        for loc in self.locations:
            if name == loc.name:
                return loc

        for npc in self.npcs:
            if name == npc.name:
                return npc

        return None

    # This needs to be changed per region
    def createLocation(self, name):
        print("Using the wrong main import")
        return None

    #This needs to be changed per region
    def createNpc(self, name):
        print("Using the wrong main import")
        return None

    # This should be ok
    def getLocation(self, name):
        loc = self.checkIn(name)

        if loc is None:
            loc = self.createLocation(name)
            self.locations.append(loc)

        return loc

    # This should be ok
    def getNpc(self, name):
        npc = self.checkIn(name)

        if npc is None:
            npc = self.createNpc(name)
            self.npcs.append(npc)

        return npc
