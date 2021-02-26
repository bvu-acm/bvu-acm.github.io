from AlexaProject.Place import Place


class placeName(Place):
    def __init__(self, person):
        # This grabs all of the methods and functions from the parent class place
        super().__init__(person)

        # Here is where you would change the variables to match you specifications
        self.name = "placeName"
        self.description = "desc"
        self.connections = []

        # The other variables are there and will be accessed based on the default, if you want to change them add them
        # here
