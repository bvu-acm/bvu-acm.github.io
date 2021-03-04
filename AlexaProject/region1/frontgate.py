from AlexaProject.Place import Place
from AlexaProject.region1.fgcl import FGCL


class frontGate(Place):
    def __init__(self, person):
        # This grabs all of the methods and functions from the parent class place
        super().__init__(person)

        # Here is where you would change the variables to match you specifications
        self.name = "front gate"
        self.description = "You stand in front of a huge gate with the words speak friend and enter spray" \
                           "\npainted on the door. "
        self.connections = ["parking lot"]

        self.comline = FGCL(person.comline.mi)

        # The other variables are there and will be accessed based on the default, if you want to change them add them
        # here
