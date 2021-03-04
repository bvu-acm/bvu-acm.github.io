from AlexaProject.commandprompt import commandLine


class FGCL(commandLine):
    def __init__(self, m):
        super().__init__()
        self.commandLine = 1
        self.mi = m

    def extraCommand(self, comstrlst, person, place):
        if comstrlst == ["speak", "friend"]:
            self.speak(place)
            return True
        return False

    def speak(self, place):
        if "main entrance" not in place.connections:
            print("You speak the word friend and the gate opens!")
            place.connections.append("main entrance")
            self.display(place)
        else:
            print("The door is already open")
