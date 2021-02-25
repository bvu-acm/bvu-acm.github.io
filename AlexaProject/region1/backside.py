from AlexaProject.Place import Place
import rightside
import leftside


class backSide(Place):
    def __init__(self):
        # This grabs all of the methods and functions from the parent class place
        super().__init__()

        # Here is where you would change the variables to match you specifications
        self.name = "back side of the building"
        self.description = "You have finally made it to the back of the building. " \
                           "\nThere is something shinning in the dirt"
        self.connections = [rightside.rightSide(), leftside.leftSide()]
        self.items = ["shinny note"]

        # The other variables are there and will be accessed based on the default, if you want to change them add them
        # here
