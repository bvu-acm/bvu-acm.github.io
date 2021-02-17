import Place
import saveload

class Person:
    def __init__(self, u="user", p="start"):
        # These defaults will need to change as you edit the dictionaries
        # Also here is where you will add inventory dictionary, health, etc
        # any player info should go here
        self.name = u
        self.location = saveload.loadPlace(u,p)
