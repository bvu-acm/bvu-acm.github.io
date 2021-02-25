from AlexaProject.Place import Place
import AlexaProject.region1.mainimportr1 as mir1

class region1Place(Place):
    def __init__(self, person):
        # This grabs all of the methods and functions from the parent class place
        super().__init__()

        # Here is where you would change the variables to match you specifications
        self.name = "placeName"
        self.description = "desc"
        self.connections = []
        if person.comline.mi is None:
            person.comline.mi = mir1.mainImportR1(person)

        # The other variables are there and will be accessed based on the default, if you want to change them add them
        # here
