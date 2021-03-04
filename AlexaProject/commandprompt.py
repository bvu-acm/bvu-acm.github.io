class commandLine(object):

    # Just a dummy init
    def __init__(self):
        self.commandLine = 0

        # This is used to keep track of all of the location imports. None by default for now change based on region
        self.mi = None

    # This function is for fast acess to areas of your region. Should be removed when we get done
    def jumpTo(self, person, place):
        place = place.replace("-", " ")
        nextloc = self.mi.getLocation(place)
        if nextloc:
            person.location = nextloc
            person.comline = person.location.comline
            self.display(person.location)
        else:
            print("%s has not been implemented yet" % place,
                  "\n1. The file itself doesn't exist yet or"
                  "\n2. The instantiation has not been added to the main import file or"
                  "\n3. The main import file for your region has not been made yet, refer to region1 for examples")

    def displayHelp(self):
        print("The available commands are:")
        print("\tsave\n\thelp\n\ttake <item>\n\teat <item>")
        print("\tdrink <item>\n\ttalk to <person>\n\tattack with <weapon>")
        print("\tgo to <place>")

    def save(self, place, person):
        print("Not implemented yet.")
        #TODO

    def take(self, item, place, person):
        print("Not implemented yet.")
        #TODO

    def eat(self, item, place, person):
        print("Not implemented yet.")
        #TODO

    def drink(self, item, place, person):
        print("Not implemented yet.")
        #TODO

    def talkTo(self, npcnum, place, person):
        if npcnum - 1 < len(place.npcs):
            npc = self.mi.getNpc(place.npcs[npcnum - 1])
            if not npc:
                print("This person has not been implemented yet"
                      "\n1. The file itself doesn't exist yet or"
                      "\n2. The instantiation has not been added to the main import file or"
                      "\n3. The main import file for your region has not been made yet, refer to region1 for examples")
        else:
            print("That number is out of the bounds of the input. Try again")

    def attackWith(self, weapon, place, person):
        print("Not implemented yet.")
        #TODO


    def goTo(self, placenum, person):
        #TODO
        # We have talked and now will change the goTo function to take 
        # a number as an argument instead of a place name
        # we found this would be easier for the alexa to interpret

        if placenum - 1 < len(person.location.connections):
            nextloc = self.mi.getLocation(person.location.connections[placenum - 1])
            if nextloc:
                person.location = nextloc
                person.comline = person.location.comline
                self.display(person.location)
            else:
                print("This area has not been implemented yet"
                      "\n1. The file itself doesn't exist yet or"
                      "\n2. The instantiation has not been added to the main import file or"
                      "\n3. The main import file for your region has not been made yet, refer to region1 for examples")
        else:
            print("That is not a valid location. Try again")

    def display(self, location):
        # Location is a Place object
        print()

        print(location.description)

        print("Exits: ", end="")
        for i in range(len(location.connections)):
            place = location.connections[i]
            if i < len(location.connections) - 1:
                # Might need to change this to just the number if Alexa reads it funny
                print("[%d] " % (i + 1) + place, end=", ")
            else:
                print("[%d] " % (i + 1) + place)

        if len(location.items) != 0:
            print("Items: ", end="")
            for i in range(len(location.items)):
                item = location.items[i]
                if i < len(location.items) - 1:
                    # Might need to change this to just the number if Alexa reads it funny
                    print("[%d] " % (i + 1) + item, end=", ")
                else:
                    print("[%d] " % (i + 1) + item)

        if len(location.npcs) != 0:
            print("NPCs: ", end="")
            for i in range(len(location.npcs)):
                npc = location.npcs[i]
                if i < len(location.npcs) - 1:
                    # Might need to change this to just the number if Alexa reads it funny
                    print("[%d] " % (i + 1) + npc, end=", ")
                else:
                    print("[%d] " % (i + 1) + npc)
        print()

    def extraCommand(self, comstrlst, person, place):
        # Here is where we would add extra functionality if we needed to
        return False

    def processCommand(self, commandString, person, place):
        # We probably wont need place since it can be attached to the object itself. Same with person
        # self.place
        # self.person

        # command string holds the string of the given command and person is the person object that holds
        # the players info
        commandString = commandString.lower()
        commandStringLst = commandString.split()
        if len(commandStringLst) > 3:
            print("Too many arguments. We are displaying the help for you. Try again please.")
            self.displayHelp()
            return

        loneCommands = ["help", "save", "display"]
        singleCommands = ["take", "eat", "drink"]
        doubleCommands = [["talk", "to"], ["attack", "with"], ["go", "to"], ["jump", "to"]]

        if self.extraCommand(commandStringLst, person, place):
            pass
        else:
            # Commands that take no arguments
            if commandStringLst[0] in loneCommands and len(commandStringLst) == 1:
                if commandStringLst[0] == "help":
                    self.displayHelp()

                elif commandStringLst[0] == "save":
                    self.save(place, person)

                elif commandStringLst[0] == "display":
                    self.display(person.location)

            # Commands that take 1 argument
            elif commandStringLst[0] in singleCommands and len(commandStringLst) == 2:
                if commandStringLst[0] == "take":
                    self.take(commandStringLst[2], place, person)

                elif commandStringLst[0] == "eat":
                    self.eat(commandStringLst[2], place, person)

                elif commandStringLst[0] == "drink":
                    self.drink(commandStringLst[2], place, person)

            # Commands that take one argument and have two prior command words
            elif commandStringLst[:2] in doubleCommands and len(commandStringLst) == 3:
                if commandStringLst[:2] == ["talk", "to"]:
                    self.talkTo(int(commandStringLst[2]), place, person)

                elif commandStringLst[:2] == ["attack", "with"]:
                    self.attackWith(commandStringLst[2], place, person)

                elif commandStringLst[:2] == ["go", "to"]:
                    self.goTo(int(commandStringLst[2]), person)

                elif commandStringLst[:2] == ["jump", "to"]:
                    self.jumpTo(person, commandStringLst[2])
            # Catch for if the user enters a bad command
            else:
                print("That is not a valid command.")
                print('If you need help, type "help"')
