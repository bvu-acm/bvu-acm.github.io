from commandprompt import *
import Person

person = Person.Person()
display(person.location)

while True:
    inp = input("Enter a command: ")

    if inp == "exit":
        break
    else:
        command(inp, person, person.location)

print("Goodbye")