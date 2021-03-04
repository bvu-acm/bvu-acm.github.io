#THIS IS AN ABSTRACT NPC CLASS. DO NOT USE THIS DIRECTLY
from AlexaProject.NPC import NPC

class npcTemplate(NPC):
    """
    If you want to change the npcDialog do it with this format otherwise you can probably leave it alone
    class npcDialog():

        def processCommand(self, commandString, person, place):
            print("You need to implement the dialong exchange type of the npc")
    """


    def __init__(self, person):
        super().__init__(person)
        self.name = "npcTemplate"
        # Should probably add stuff to say to the dialog so I left it in
        # This is the format for speaking to the npc. Change this as you wish
        # The numbers on the far left represent how deep in a specific conversion they are
        #       e is the end of the conversation and will give control back to the user commandline
        # The inner dictionary and numbers are what the user will implement. That is the dialog of the user
        #       They choose the number just like regular command line

        self.dialog = {1: ["What the npc will say", {1: ["User voice", 2], 2: ["User voice", 2],
                                                     3: ["User voice", 2], 4: ["User voice", 2]}],
                       2: ["What the npc will say", {1: ["User voice", 3], 2: ["User voice", 3],
                                                     3: ["User voice", 3], 4: ["User voice", 3]}],
                       3: ["What the npc will say", {1: ["User voice", 4], 2: ["User voice", 4],
                                                     3: ["User voice", 4], 4: ["User voice", 4]}],
                       4: ["What the npc will say", {1: ["User voice", "e"], 2: ["User voice", "e"],
                                                     3: ["User voice", "e"], 4: ["User voice", "e"]}],
                       "e": ["What the npc will say before leaving", None]
                       }
        person.comline = self.npcDialog(self)



