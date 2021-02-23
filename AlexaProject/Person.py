import Place
import saveload
from Item import *

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


    def set_location(self, location):
        self.location = location


    # Private method that returns the object if the user has the item in their
    # inventory. Otherwise returns None
    def __has_item(self, item_name):
        has_item = False
        for item in self.inventory:
            if item_name == item.name:
                return item
        return None
        


    # Takes the name of an item specified by the user
    # Returns the result of 
    def eat(self, item_name):
        item = self.__has_item(item_name)
        #FIXME: These are all placeholders, please change
        if not item:
            return "You do not have " + item_name + " in your inventory"

        if item.item_type == "food":
            # Someone please make this more interesting
            self.hp += 5
            return item_name + " has been eaten"
        else:
            # And this is slightly mean, so... maybe change it
            self.hp -= 1
            return item_name + " is not food. You break your teeth on it"


    # Takes item name. Returns int representing the amount of damage done
    def attack(self, item_name):
        item = self.__has_item(item_name)
        if not item:
            return "You do not have " + item_name + " in your inventory"

        if item.item_type == "weapon":
            return 5
        else:
            return 0


if __name__ == "__main__":
    p = Person()
