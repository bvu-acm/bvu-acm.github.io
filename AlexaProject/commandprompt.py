import Place
import Person
import saveload

class commandLine(object):

    # Just a dummy init
    def __init__(self):
        self.commandLine = 0

    def displayHelp(self):
        print("The available commands are:")
        print("\tsave\n\thelp\n\ttake <item>\n\teat <item>")
        print("\tdrink <item>\n\ttalk to <person>\n\tattack with <weapon>")
        print("\tgo to <place>")

    def save(self, place, person):
        #TODO

    def take(self, item, place, person):
        #TODO

    def eat(self, item, place, person):
        #TODO

    def drink(self, item, place, person):
        #TODO

    def talkTo(self, npc, place, person):
        #TODO

    def attackWith(self, weapon, place, person):
        #TODO


    def goTo(self, placenum, person):
        #TODO
        # We have talked and now will change the goTo function to take 
        # a number as an argument instead of a place name
        # we found this would be easier for the alexa to interpret

        if placenum in person.location.connections:
            saveload.saveUser(person)
            person.location = saveload.loadPlace(person.name, placenum)
            display(person.location)

    def display(self, location):
        print(location.description)
        print("Exits: " + str(location.connections))

    def processCommand(self, commandString, person, place):
        # command string holds the string of the given command and person is the person object that holds
        # the players info
        commandString = commandString.lower()
        commandStringLst = commandString.split()
        if len(commandStringLst) > 3:
            print("Too many arguments. We are displaying the help for you. Try again please.")
            self.displayHelp()
            return 
        loneCommands = ["help", "save"]
        singleCommands = ["take", "eat", "drink"]
        doubleCommands = [["talk", "to"], ["attack", "with"], ["go", "to"]]

        # Commands that take no arguments
        if commandStringLst[0] in loneCommands and len(commandStringLst) == 1:
            if commandStringLst[0] == "help":
                self.displayHelp()

            elif commandStringLst[0] == "save":
                self.save(place, person)

        # Commands that take 1 argument
        elif commandStringlstLst[0] in singleCommands and len(commandStringLst) == 2:
            if commandStringLst[0] == "take":
                self.take(commandStringLst[2], place, person)

            elif commandStringLst[0] == "eat":
                self.eat(commandStringLst[2], place, person)

            elif commandStringLst[0] == "drink":
                self.drink(commandStringLst[2], place, person)

        # Commands that take one argument and have two prior command words
        elif commandStringLst[:1] in doubleCommands and len(commandStringLst) == 3:
            if commandStringLst[:1] == ["talk", "to"]:
                self.talkTo(commandStringLst[2], place, person)

            elif commandStringLst[:1] == ["attack", "with"]:
                self.attackWith(commandStringLst[2], place, person)

            elif commandStringLst[:1] == ["go", "to"]:
                self.goTo(commandStringLst[2], person)

        # Catch for if the user enters a bad command
        else:
            print("That is not a valid command.")
            print('If you need help, type "help"')
