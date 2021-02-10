import people


def command(commandString, person):
    # command string holds the string of the given command and person is the person object that holds
    # the players info

    # For ide debugging purposes
    # commandString = ""

    # I am putting this in a variables because it will allow us to change it later if we want the words
    # to be different
    com1 = "go to"
    com2 = "display"
    if com1 in commandString:
        place = commandString[len(com1) + 1:]
        goto(place, person)
    elif com2 in commandString:
        display(person.location)


def goto(place, person):
    if place in people.connections[person.location]:
        person.location = place
        display(place)


def display(location):
    print(people.descriptions[location])
    print(people.connections[location])
