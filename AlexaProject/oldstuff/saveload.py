import os
import pathlib
import Place
import Person


def saveUser(user):
    # user is a person object
    # We will need to continuously add to this as we add more stuff likes items and such

    try:
        p = os.path.join(os.path.abspath(os.getcwd()), "savefiles")
        fp = os.path.join(p, user.name)
        os.mkdir(fp)
        print("'" + user.name + "' folder has been created")
    except:
        print("The save folder already exists")

    s = pathlib.Path.cwd()
    b = os.path.join(s, "savefiles")
    t = os.path.join(b, user.name)
    fp = os.path.join(t, user.name + ".txt")

    check = True
    try:
        f = open(fp, "r")
        rl = f.readlines()
        f.close()

        fp2 = os.path.join(t, user.name + "backup.txt")
        f = open(fp2, "w")
        for item in rl:
            f.write(item)
        f.close()
    except:
        print("This is the first time saving")
        check = False

    f = open(fp, "w")
    f.write(user.name + "\n")
    f.write(user.location.name + "\n")
    f.close()
    if check:
        print("Re-writing the save")

    savePlace(user, user.location)


def loadUser(username):
    user = Person.Person()
    s = pathlib.Path.cwd()
    b = os.path.join(s, "savefiles")
    t = os.path.join(b, username)
    fp = os.path.join(t, username + ".txt")

    try:
        f = open(fp, "r")
        rl = f.readlines()
        f.close()

        user.name = rl[0].rstrip()
        placename = rl[1].rstrip()
        user.location = loadPlace(username, placename)

    except:
        print("The user save you are trying to load does not exist")

    return user


def savePlace(user, place):
    # place is the place object
    # user is the person object

    s = pathlib.Path.cwd()
    b = os.path.join(s, "savefiles")
    t = os.path.join(b, user.name)
    fp = os.path.join(t, place.name + ".txt")

    check = True

    try:
        f = open(fp, "r")
        rl = f.readlines()
        f.close()

        fp2 = os.path.join(t, place.name + "backup.txt")
        f = open(fp2, "w")
        for item in rl:
            f.write(item)
        f.close()

        print("The place file exits")
    except:
        print("Creating the place file")
        check = False

    f = open(fp, "w")
    f.write(place.name + "\n")
    f.write(place.description + "\n")
    lst = ""
    for item in place.connections:
        lst += item + ","
    f.write(lst + "\n")
    if check:
        print("Re-writting the place file save")


def loadPlace(username, placename):
    # works like save but in reverse
    place = Place.Place()

    s = pathlib.Path.cwd()
    b = os.path.join(s, "savefiles")
    t = os.path.join(b, username)
    fp = os.path.join(t, placename + ".txt")

    try:
        f = open(fp, "r")
        rl = f.readlines()
        f.close()

        # add place. to all below
        place.name = rl[0].rstrip()
        place.description = rl[1].rstrip()
        place.connections = rl[2].split(",")
        place.connections.pop()

    except:
        print("The place file '" + placename + "' does not exist")
        print("Opening default")

        a = pathlib.Path.cwd()
        b = os.path.join(a, "savefiles")
        c = os.path.join(b, "basesaves")
        fp = os.path.join(c, placename + ".txt")

        try:
            f = open(fp, "r")
            rl = f.readlines()
            f.close()

            # add place. to all below
            place.name = rl[0].rstrip()
            place.description = rl[1].rstrip()
            place.connections = rl[2].split(",")
            place.connections.pop()

        except:
            print("The base place file '" + placename + "' does not exist. It needs to be created")


    return place
