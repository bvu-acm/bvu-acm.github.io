from AlexaProject.mainimport import mainImport


class mainImportR1(mainImport):

    def __init__(self, p):
        super().__init__()
        self.person = p


    def createLocation(self, name):
        # This system seems like it could get out of hand fast. May need to change it

        if name == "left side of the building":
            from AlexaProject.region1.leftside import leftSide
            return leftSide(self.person)
        elif name == "right side of the building":
            from AlexaProject.region1.rightside import rightSide
            return rightSide(self.person)
        elif name == "front gate":
            from AlexaProject.region1.frontgate import frontGate
            return frontGate(self.person)
        elif name == "back side of the building":
            from AlexaProject.region1.backside import backSide
            return backSide(self.person)
        elif name == "parking lot":
            from AlexaProject.region1.parkinglot import parkingLot
            return parkingLot(self.person)
