# from commandprompt import *
import Person
# This will hopefully not be needed later
from AlexaProject.region1.parkinglot import parkingLot
from AlexaProject.region1.mainimportr1 import mainImportR1

person = Person.Person()
# This is added for me to start in region one. It will be changed to the default location when we are done
person.location = parkingLot(person)
person.comline.mi.locations.append(person.location)
# person.location =

# Again the double location stuff seems a bit redundant
person.comline.display(person.location)

while True:
    inp = input("Enter a command: ")

    if inp == "exit":
        break
    else:
        # command(inp, person, person.location)
        person.comline.processCommand(inp, person, person.location)

print("Goodbye")