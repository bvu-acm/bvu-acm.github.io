from AlexaProject.commandprompt import commandLine


class FGCL(commandLine):
    def __init__(self, m):
        super().__init__()
        self.commandLine = 1
        self.mi = m

    def extraCommand(self, comstrlst):
        if comstrlst == ["speak", "friend"]:
            self.speak()
            return True
        return False

    def speak(self):
        print("You speak the word friend and the gate opens!!"
              "\njust kidding I haven't implemented that yet :)")
