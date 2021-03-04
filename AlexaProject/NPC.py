#THIS IS AN ABSTRACT NPC CLASS. DO NOT USE THIS DIRECTLY
from AlexaProject.commandprompt import commandLine


class NPC:
    class npcDialog:
        def __init__(self, n):
            self.deep = 1
            self.npc = n
            print(self.npc.dialog[self.deep][0])
            iter = 1
            for key in self.npc.dialog[self.deep][1]:
                print("[" + str(iter) + "]: " + self.npc.dialog[self.deep][1][key][0])
                iter += 1

        def processCommand(self, commandString, person, place):
            # The command string should only be a number so I will try to parse it right away
            command = -1
            try:
                spl = commandString.split()
                if len(spl) != 1:
                    None.barf()
                command = int(commandString)
            except:
                print("This was not an acceptable response")

            if command != -1 and command < len(self.npc.dialog[self.deep][1]):
                self.deep = self.npc.dialog[self.deep][1][command][1]
                print(self.npc.dialog[self.deep][0])
                if self.deep != "e":
                    iter = 1
                    for key in self.npc.dialog[self.deep][1]:
                        print("[" + str(iter) + "]: " + self.npc.dialog[self.deep][1][key][0])
                        iter += 1
                else:
                    print("You exit the conversation")
                    self.npc.person.comline = self.npc.commandLine
                    self.npc.commandLine.display(self.npc.person.location)

    def __init__(self, person):
        self.person = person
        self.name = "npcName"
        self.hp = 25
        # The inventory is the items they drop
        self.inventory = []
        self.dialog = {}
        # This is to switch back to once the player is done talking to the NPC
        self.commandLine = person.comline
        # This has to go on the template because if it doesn't it breaks
        # person.comline = self.npcDialog(self)



