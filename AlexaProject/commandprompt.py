import places

def command(commandString, person):
    # command string holds the string of the given command and person is the person object that holds
    # the players info

    # For ide debugging purposes
    # commandString = ""
    commandString = commandString.lower()
    commandStringLst = commandString.split()

    loneCommands = ["help", "hunt", "save", "run away", "sleep"]
    singleCommands = ["take", "eat", "drink"]
    doubleCommands = [["talk", "to"], ["attack", "with"], ["trade", "with"], ["go", "to"]]

    if commandString in loneCommands:
        if commandString == "help":
            displayHelp()

        if commandString == "hunt":

        if commandString == "save":

        if commandString == "run away":

        if commandString == "sleep":


    elif commandStringlst[0] in singleCommands:

    elif commandStringlst[:1] in doubleCommands:
        
    else:
        print("That is not a valid command.")
        print('If you need help, type "help"')


def goto(place, person):
    if place in places.connections[person.location]:
        person.location = place
        display(place)


def display(location):
    print(places.descriptions[location])
    print(places.connections[location])

def displayHelp():
    print("The available commands are:")
    print("\thunt\n\tsave\n\trun away\n\tsleep\n\ttake 'item'\n\teat 'item'")
    print("\tdrink 'item'\n\ttalk to 'person'\n\tattack with 'weapon'")
    print("\ttrade with 'person'\n\tgo to 'place'")
