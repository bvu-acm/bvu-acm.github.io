import os
import pathlib
def saveUser(user):
    # user right now is the name of the user. could later be the person object
    # We will need to continuously add to this as we add more stuff likes items and such

    place = "name"
    try:
        p = os.path.join(os.path.abspath(os.getcwd()), "savefiles")
        fp = os.path.join(p, user)
        os.mkdir(fp)
        print("'" + user + "' folder has been created")
    except:
        print("The save folder already exists")

    s = pathlib.Path.cwd()
    b = os.path.join(s, "savefiles")
    t = os.path.join(b, user)
    fp = os.path.join(t, user + ".txt")

    check = True
    try:
        f = open(fp, "r")
        # This is just in case the function messes something up
        rl = f.readlines()
        f.close()

        fp2 = os.path.join(t, user + "backup.txt")
        f = open(fp2, "w")
        for item in rl:
            f.write(item + "\n")
        f.close()
    except:
        print("This is the first time saving")
        check = False


    f = open(fp, "w")
    f.write(user + "\n")
    f.write(place + "\n")
    f.close()
    if check:
        print("Re-writing the save")

    savePlace(user, place)
def loadUser(username):
    user = None
    s = pathlib.Path.cwd()
    b = os.path.join(s, "savefiles")
    t = os.path.join(b, username)
    fp = os.path.join(t, username + ".txt")

    try:
        f = open(fp, "r")
        # This is just in case the function messes something up
        rl = f.readlines()
        f.close()

        # add user. to name only
        name = rl[0].rstrip()
        place = rl[1].rstrip()
        # add user.
        place = loadPlace(username, place)

    except:
        print("The user save you are trying to load does not exist")

    return user

def savePlace(user, place):
    # place is the place object
    # For now the attributes will be put at the start

    name = "name"
    description = "desc"
    connections = ["one", "two", "three"]


    s = pathlib.Path.cwd()
    b = os.path.join(s, "savefiles")
    t = os.path.join(b, user)
    fp = os.path.join(t, name + ".txt")

    check = True

    try:
        f = open(fp, "r")
        # This is just in case the function messes something up
        rl = f.readlines()
        f.close()

        fp2 = os.path.join(t, name + "backup.txt")
        f = open(fp2, "w")
        for item in rl:
            f.write(item + "\n")
        f.close()

        print("The place file exits")
    except:
        print("Creating the place file")
        check = False


    f = open(fp, "w")
    f.write(name + ":\n")
    f.write(description + "\n")
    lst = ""
    for item in connections:
        lst += item + ","
    f.write(lst + "\n")
    if check:
        print("Re-writting the place file save")

def loadPlace(username, placename):
    # works like save but in reverse
    # Since we have not made the place object it is a none type
    # It will be returned later as an object
    place = None

    s = pathlib.Path.cwd()
    b = os.path.join(s, "savefiles")
    t = os.path.join(b, username)
    fp = os.path.join(t, placename + ".txt")

    try:
        f = open(fp, "r")
        rl = f.readlines()
        f.close()

        # add place. to all below
        name = rl[0].rstrip()
        desc = rl[1].rstrip()
        cons = rl[2].split(",")
        cons.pop()

    except:
        print("The place file '" + placename + "' does not exist")

    return place


saveUser("trial")
loadUser("trial")