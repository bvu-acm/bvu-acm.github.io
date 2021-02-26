from AlexaProject.Place import Place
import AlexaProject.region1.mainimportr1 as mir1


class parkingLot(Place):
    def __init__(self, person):
        # This grabs all of the methods and functions from the parent class place
        super().__init__(person)

        # Here is where you would change the variables to match you specifications
        self.name = "parking lot"
        self.description = "You have suddenly appeared in the parking lot of Apple Headquarters. Steve jobs is standing" \
                           "\non the roof laughing at you. You look around and see an entrance gate in front of you."

        self.connections = ["left side of the building", "right side of the building", "front gate"]
        self.items = ["broken apple phone", "chips", "steves tears"]

        person.comline.mi = mir1.mainImportR1(person)

        # The other variables are there and will be accessed based on the default, if you want to change them add them
        # here
