from AlexaProject.Place import Place
import parkinglot
import backside


class rightSide(Place):
    def __init__(self):
        # This grabs all of the methods and functions from the parent class place
        super().__init__()

        # Here is where you would change the variables to match you specifications
        self.name = "right side of the building"
        self.description = "You walk along the left side of the silver donut. It seems to go on forever"
        self.connections = [parkinglot.parkingLot(), backside.backSide()]

        # The other variables are there and will be accessed based on the default, if you want to change them add them
        # here
