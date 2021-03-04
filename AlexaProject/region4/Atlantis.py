Sign = ("""
      
    ___   __  __            __  _     
   /   | / /_/ /___ _____  / /_(_)____
  / /| |/ __/ / __ `/ __ \/ __/ / ___/
 / ___ / /_/ / /_/ / / / / /_/ (__  ) 
/_/  |_\__/_/\__,_/_/ /_/\__/_/____/  
                                      

""") # Ignore the fancy text art (its a leftover from my last text adventure)

Win = ("""
__  __               _       ___          __
\ \/ /___  __  __   | |     / (_)___     / /
 \  / __ \/ / / /   | | /| / / / __ \   / / 
 / / /_/ / /_/ /    | |/ |/ / / / / /  /_/  
/_/\____/\__,_/     |__/|__/_/_/ /_/  (_)   
                                            
""")
GameOver =("""

   ______                        ____                     __
  / ____/___ _____ ___  ___     / __ \_   _____  _____   / /
 / / __/ __ `/ __ `__ \/ _ \   / / / / | / / _ \/ ___/  / / 
/ /_/ / /_/ / / / / / /  __/  / /_/ /| |/ /  __/ /     /_/  
\____/\__,_/_/ /_/ /_/\___/   \____/ |___/\___/_/     (_)   
                                                            
""")
import sys
descriptions = {
    "NorthEntrance" : "This is the north entrance to Atlantis. The city appears to be protected by some sort of force field. Two armored mermaid guards block the entrance.",
    "SouthEntrance" : "This is the south entrance to Atlantis. This entrance is blocked by boulders. There does not seem to be anything here.",
   
   

         
}
NPCs = {
    "NorthEntrance" : ["Armored Mermaid"],
    "SouthEntrance" : [],
    
   

    }
exits = {
    "NorthEntrance" : ["South Entrance"],
    "SouthEntrance" : ["North Entrance"],
    
  
}
items = {
    "NorthEntrance" : ["trident", "map"],
    "SouthEntrance" : ["rock", "seaweed"],
   

}
Weapons = ["rock", "trident"]
Food = ["blue apple", "seaweed"] # this is a running joke from my last game
Drink = ["water"] # warning don't eat the blue apple lol
Misc = ["map"]
inventory = [
    ["*Weapons*"],[],
    ["*Misc*"],[],
    ["*Food*"],[],
    ["*Drinks*"],[],
    ]

def look():
    global place
    print(descriptions[place])
    print("Items here: %s" % ", ".join(items[place]))
    print("Exits: %s" % ", ".join(exits[place]))
    print("NPCs: %s" % ", ".join(NPCs[place]))

def goto(nextplace):
    global place
    if nextplace in exits[place]:
        place = nextplace
        print("You are now in %s." % place)
        hearts()
        look()
    else:
        print("Sorry, I don't see '%s' from here." % nextplace)

def take(item):
    global place
    if item in items[place]:
        if item == "water":
            print("There is infinite water.")
            inventory[5].append(item)
        else:
            items[place].remove(item)
            if item in (Weapons):
                inventory[1].append(item)
            elif item in (Misc):
                inventory[3].append(item)
            elif item in (Food):
                inventory[5].append(item)
            elif item in (Drink):
                inventory[7].append(item)
    else:
        print("Sorry, I don't see that here.")
        
def drop(item):
    global place
    if item in inventory[1]:
        inventory[1].remove(item)
        items[place].append(item)
        print("You have dropped %s." % item)
    elif item in inventory[3]:
        inventory[3].remove(item)
        items[place].append(item)
        print("You have dropped %s." % item)
    elif item in inventory[5]:
        inventory[5].remove(item)
        items[place].append(item)
        print("You have dropped %s." % item)
    elif item in inventory[7]:
        inventory[7].remove(item)
        items[place].append(item)
        print("You have dropped %s." % item)
    else:
        print("Sorry, you don't have %s." % item)
        
def eat(item):
    global place
    import random
    if item in inventory[1]:
        print("Eating a %s? What's wrong with you?" %(item))
    elif item in inventory[3]:
        print("Eating a %s? What's wrong with you?" %(item))
    elif item in inventory[5]:
        if item == "blue apple":
            eat_apple = input("This apple seems strange are you sure you want to eat it?... yes/no : ")
            if eat_apple == "yes":
                blue = random.randint(1,3)
                if blue == 1:
                    print("You blacked out due to strange effects from the apple.")
                    inventory[5].remove(item)
                    player["health"]= player["health"] - 20
                    hearts()
                elif blue == 2:
                    print("You eat the %s and now you have full health")
                    print("Nothing strange happened...")
                    inventory[5].remove(item)
                    player["health"] = 25
                    hearts()
                elif blue == 3:
                    print("You shouldn't eat strange fruit... alergic reaction?... poison?...")
                    print("This is the end of the road...")
                    print(GameOver)
                    sys.exit()
            if eat_apple == "no":
                print("You decided against eating the apple.")
        else:
            print("You eat the %s and now you have full health" %(item))
            inventory[5].remove(item)
            player["health"] = 25
            hearts()
    elif item in inventory[7]:
        print("What are you doing? You can't eat %s, %s is a drink." %(item, item))
        
def drink(item):
    global place
    if item in inventory[1]:
        print("Drinking a %s? What's wrong with you?" %(item))
    elif item in inventory[3]:
        print("Drinking a %s? What's wrong with you?" %(item))
    elif item in inventory[5]:
        print("What are you doing? You can't drink %s, %s is a solid food." %(item, item))
    elif item in inventory[7]:
        print("You drink the %s and now you have full health" %(item))
        inventory[7].remove(item)
        player["health"] = 25
        hearts()
def hearts():
    global place
    if player["health"] == 25:
        print("Current health: 25")
    elif player["health"] == 24:
        print("Current health: 24")
    elif player["health"] == 23:
        print("Current health: 23")
    elif player["health"] == 22:
        print("Current health: 22")
    elif player["health"] == 21:
        print("Current health: 21")
    elif player["health"] == 20:
        print("Current health: 20")
    elif player["health"] == 19:
        print("Current health: 19")
    elif player["health"] == 18:
        print("Current health: 18")
    elif player["health"] == 17:
        print("Current health: 17")
    elif player["health"] == 16:
        print("Current health: 16")
    elif player["health"] == 15:
        print("Current health: 15")
    elif player["health"] == 14:
        print("Current health: 14")
    elif player["health"] == 13:
        print("Current health: 13")
    elif player["health"] == 12:
        print("Current health: 12")
    elif player["health"] == 11:
        print("Current health: 11")
    elif player["health"] == 10:
        print("Current health: 10")
    elif player["health"] == 9:
        print("Current health: 9")
    elif player["health"] == 8:
        print("Current health: 8")
    elif player["health"] == 7:
        print("Current health: 7")
    elif player["health"] == 6:
        print("Current health: 6")
    elif player["health"] == 5:
        print("Current health: 5")
    elif player["health"] == 4:
        print("Current health: 4")
    elif player["health"] == 3:
        print("Current health: 3")
    elif player["health"] == 2:
        print("Current health: 2")
    elif player["health"] == 1:
        print("Current health: 1")
    elif player["health"] <=0:
        print("You died.")
        print(GameOver)
        sys.exit()
        
        

def attack(NPC, Weapon):
    global place
    import random
    NPC_health = 15
    health = player["health"]
    if (Weapon) in inventory[1]:
        while NPC_health !=0:
            hit = random.randint(1,2)
            if hit == 1:
                print("You attack the %s with the %s" % (NPC, Weapon))
                NPC_health = NPC_health -1
                if NPC_health == 0:
                    print("The %s is dead" % (NPC))
                    NPCs[place].remove(NPC)
                    break
                
            elif hit == 2:
                print("You attemted to attack but missed.")
            attackback = random.randint(1, 3)
            if attackback == 1:
                print ("%s attacked you back you lose 1 health point." %(NPC))
                player["health"] = player["health"] -1
                hearts()
                if player["health"] < 1:
                    break 
                
            elif attackback == 2 or 3:
                print ("%s attempted to attack you but missed." %(NPC))
    elif (Weapon) in items[place]:
        print("You do not have a weapon by that name")
    elif (Weapon) in inventory[5]:
        print("Attack with %s? That's absurd." %(Weapon))
    elif (Weapon) in inventory[7]:
        print("Attack with %s? That's absurd." %(Weapon))
    elif (Weapon) in inventory[3]:
        print("Attack with %s? That's absurd." %(Weapon))
    elif (Weapon) not in inventory[0:]:
        print("You do not have a weapon by that name.")
print(Sign)
print("For a list of commands you can use type 'commands' ")          
player = {"health": None}        
place = "NorthEntrance"
player["health"] = 25
healthcheck = int(player["health"])
hearts()
look()

while True:
    
    command = input("Command? ")
    if (player["health"])<= 0:
        break
    if command == "look":
        look()
    elif command.startswith("go to "):             
        nextplace = command[6:]                        
        goto(nextplace)
    elif command.startswith("take "):
        loot = command[5:]
        take(loot)
    elif command.startswith("drop "):
        loot = command[5:]
        drop(loot)
    elif command.lower() in ["quit", "exit", "bye", "get me out of here"]:
        print("Okay, fine, you quitter.")
        print(GameOver)
        break
    elif command.lower() == "inventory":
        print("You currently possess:")
        for item in inventory:
            print(item)
    elif command.startswith("attack "):
        with_index = command.find("with ")
        NPC = command[len("attack "):with_index-1]
        Weapon = command[with_index+len("with "):]
        if NPC in NPCs[place]:
            attack(NPC, Weapon)
        elif NPC not in NPCs[place]:
            print("There is no %s here." %(command[7:]))
    elif command.startswith("talk "):
        to_index = command.find("to ")
        talk = command[len("talk "):to_index-1]
        NPC = command[to_index+len("to "):]
        if NPC in NPCs[place]:
            print ("You talk to %s." %NPC)
            if NPC == "Armored Mermaid":
                talk1 = input ("What do you want..? ")
                if talk1 == "Let me in":
                    talk2 = input ("Why should I let you in? ")
                    if talk2 == ("Because"):
                        print("That is not a good enough answer! ")
                elif talk1 == "Nothing":
                    print ("Then why are you still talking to me...? Leave! ")
                
        elif NPC not in NPCs[place]:
            print("There is no %s here." %(command[7:]))
    elif command == "check health":
        hearts()
    elif command.startswith("eat "):
        item = command[4:]
        eat(item)
    elif command.startswith("drink "):
        item = command[6:]
        drink(item)
    elif command == "commands":
        print ("""Commands: look, go to, talk to, take, drop, quit, bye, get me out of here,
inventory, attack, check health, eat, drink, commands""")
    else:
        print("Sorry, I don't recognize that command.")
    
print("Thanks for playing.")