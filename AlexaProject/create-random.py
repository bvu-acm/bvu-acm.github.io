# This file will create a true skeleton outline of the places dictionaries that
# will also hold all of the connections

# The two dictionaries that I will be making are the places as keys to the description and
# a connections dictionary with the places as a key and a list of possible connections as the value

desc = "descriptions = {\n"
cons = "connections = {\n"

# This is the number that will dictate the total length of the 'true path' of the game
mainConNumber = 25

for i in range(mainConNumber):

    name1 = "name" + str(i)

    if i < mainConNumber - 1:

        name2 = "name" + str(i + 1)

        desc += '    "' + name1 + '": ' + '"' + name1 + '",\n'
        cons += '    "' + name1 + '": ' + '["' + name2 + '"],\n'
    else:
        desc += '    "' + name1 + '": ' + '"' + name1 + '",\n'

desc += "}\n"
cons += "}\n"

f = open("places.py", "w")
f.write(desc + "\n")
f.write(cons + "\n")

print("done")
