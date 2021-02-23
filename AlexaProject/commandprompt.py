import Place
import Person
import saveload

def command(commandString, person, place):
    # command string holds the string of the given command and person is the person object that holds
    # the players info

    # For ide debugging purposes
    # command = ""
    commandString = commandString.lower()
    commandStringLst = commandString.split()

    loneCommands = ["help", "hunt", "save", "run away", "sleep"]
    singleCommands = ["take", "eat", "drink"]
    doubleCommands = [["talk", "to"], ["attack", "with"], ["trade", "with"], ["go", "to"]]

    # Commands that take no arguments
    if commandStringLst[0] in loneCommands:
        if commandStringLst[0] == "help":
            displayHelp()

        if commandStringLst[0] == "hunt":

        if commandStringLst[0] == "save":

        if commandStringLst[0] == "run away":

        if commandStringLst[0] == "sleep":

    # Commands that take 1 argument
    elif commandStringlstLst[0] in singleCommands:
        if commandStringLst[0] == "take":

        if commandStringLst[0] == "eat":

        if commandStringLst[0] == "drink":

    # Commands that take one argument and have two prior command words
    elif commandStringLst[:1] in doubleCommands:
        if commandStringLst[:1] == ["talk", "to"]:

        if commandStringLst[:1] == ["attack", "with"]:

        if commandStringLst[:1] == ["trade", "with"]:

        if commandStringLst[:1] == ["go", "to"]:
            goto(commandStringLst[2], person)

    # Catch for if the user enters a bad command
    else:
        print("That is not a valid command.")
        print('If you need help, type "help"')

def goto(placename, person):
    if placename in person.location.connections:
        saveload.saveUser(person)
        person.location = saveload.loadPlace(person.name, placename)
        display(person.location)

def display(location):
    print(location.description)
    print("Exits: " + str(location.connections))

def displayHelp():
    print("The available commands are:")
    print("\thunt\n\tsave\n\trun away\n\tsleep\n\ttake 'item'\n\teat 'item'")
    print("\tdrink 'item'\n\ttalk to 'person'\n\tattack with 'weapon'")
    print("\ttrade with 'person'\n\tgo to 'place'")
