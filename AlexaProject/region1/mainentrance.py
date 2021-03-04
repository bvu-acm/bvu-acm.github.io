from AlexaProject.Place import Place


class mainentrance(Place):
    def __init__(self, person):
        # This grabs all of the methods and functions from the parent class place
        super().__init__(person)

        # Here is where you would change the variables to match you specifications
        self.name = "main entrance"
        self.description = "You walk into a big rotunda much bigger than the science centers back home" \
                           "\nYou look around and see a robot at the front gate and three doors on each corner" \
                           "\n of the room"
        self.connections = ["front gate", "conference room 1", "conference room 2", "main hallway"]
        self.items = ["desk computer", "desk monitor", "pen", "paperwork"]
        self.npcs = ["robot secretary"]

        # The other variables are there and will be accessed based on the default, if you want to change them add them
        # here
