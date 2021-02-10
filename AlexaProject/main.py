from commandprompt import *
import Person

print("hello world")

person = Person.Person()
display(person.location)

while True:
    inp = input("Enter a command: ")

    if inp == "exit":
        break
    else:
        command(inp, person)

print("Goodbye")