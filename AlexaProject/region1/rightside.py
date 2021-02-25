from AlexaProject.region1.region1place import region1Place


class rightSide(region1Place):

    def __init__(self, person):
        # This grabs all of the methods and functions from the parent class place
        super().__init__(person)

        # Here is where you would change the variables to match you specifications
        self.name = "right side of the building"
        self.description = "You walk along the right side of the silver donut. It seems to go on forever"
        self.connections = ["parking lot", "back side of the building"]

        # The other variables are there and will be accessed based on the default, if you want to change them add them
        # here
