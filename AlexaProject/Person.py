import Place
# import saveload

# I took this one out for now until we get the item files made
# from Item import *
from AlexaProject.commandprompt import commandLine

'''

CHANGES TO MAKE IN OTHER CLASSES:
    Item must have a name and a item_type
    Item item_types include: ['food', 'weapon']
    I would also suggest adding a dictionary representing item traits

'''


class Person:
    def __init__(self, u="user", p="start"):
        # These defaults will need to change as you edit the dictionaries
        # Also here is where you will add inventory dictionary, health, etc
        # any player info should go here
        self.location = "name0"
        self.hp = 25
        self.inventory = []
        self.comline = commandLine()



if __name__ == "__main__":
    p = Person()
