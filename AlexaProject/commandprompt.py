import Place
import saveload


def command(commandString, person, place):
    # command string holds the string of the given command and person is the person object that holds
    # the players info

    # For ide debugging purposes
    # commandString = ""

    # I am putting this in a variables because it will allow us to change it later if we want the words
    # to be different
    com1 = "go to"
    com2 = "display"
    if com1 in commandString:
        placename = commandString[len(com1) + 1:]
        goto(placename, person)
    elif com2 in commandString:
        display(person.location)


def goto(placename, person):
    if placename in person.location.connections:
        saveload.saveUser(person)
        person.location = saveload.loadPlace(person.name, placename)
        display(person.location)


def display(location):
    print(location.description)
    print("Exits: " + str(location.connections))
