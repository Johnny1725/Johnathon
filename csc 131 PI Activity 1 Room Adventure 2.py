###################################
##Name:Johnathon Terry
##Date:1/21/2020
##Program:Pi Activity:Room Adventure
##################################3
import random

print random.randint(0,10)
#the blueprint for a room
class Room(object):
    #the constructor
    def __init__(self, name):
        self.name = name
        self.exits = {}
        self.items = {}
        self.grabbables = []
        
    # getters and setters for the instance variables 
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    @property
    def exits(self):
        return self._exits
    @exits.setter
    def exits(self, value):
        self._exits = value


    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, value):
        self._items = value

    @property
    def grabbables(self):
        return self._grabbables
    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value
        
    #add an exit to the room
    def addExit(self, exit, room):
        self._exits[exit] = room

    #adds an item to the room 
    def addItem(self, item, desc):
        self._items[item] = desc

    #adds a grabbable item to the room
    def addGrabbable (self, item):
        self._grabbables.append(item)

    #removes a grabbable item from the room
    def delGrabbable(self, item):
        self._grabbables.remove(item)

    #returns a string description of the room
    def __str__(self):
        s = "you are in {}.\n".format(self.name)
        s += "You see: "
        for item in self.items.keys():
            s += item + " "
        s += "\n"
        s += "Exits: "
        for exit in self.exits.keys():
            s += exit + " "
        return s

##########
#START THE GAME

# creates the rooms
def createRooms():
    # current room needs to be a global because it will be changed in the main part of the program
    global currentRoom

    # creates the rooms and gives them names
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")

    #add Exits, Grabbables, and Items to room 1
    r1.addExit("east", r2)
    r1.addExit("south", r3)
    r1.addGrabbable("key")
    r1.addItem("chair", "It is made of wicker and no one is sitting on it.")
    r1.addItem("table", "It is made of oak. A golden key rests on it.")
    #Items that I added and made observable in room 1
    r1.addItem("sofa", "It looks nice")
    r1.addGrabbable("comb")

    #add Exits and Items to room 2
    r2.addExit("west", r1)
    r2.addExit("south", r4)
    r2.addItem("rug", "It is nice and Indian. It also needs to be vacuumed.")
    r2.addItem("fireplace", "It is full of ashes")
    #Items that I added and made observable in room 2
    r2.addItem("TV", "It is a really nice flat screen that is a 72inch")
    r2.addGrabbable("Lighter")

    #add Exits, Grabbables, and Items to room 3
    r3.addExit("north", r1)
    r3.addExit("east", r4)
    r3.addGrabbable("book")
    r3.addItem("bookshelves", "They are empty. Go figure.")
    r3.addItem("statue", "There is nothing special about it.")
    r3.addItem("desk", "The statue is resting on it. So is a book.")
    #Items that I added and made observable in room 3
    r3.addItem("mirror", "It needs to be cleaned.")
    r3.addGrabbable("windex") 

    #add Exits, Grabbables, and Items to room 4
    r4.addExit("north", r2)
    r4.addExit("west", r3)
    r4.addExit("south", None)
    r4.addGrabbable("6-pack")
    r4.addItem("brew_rig", "Gourd is brewing some sort of oatmeal stout on the brew rig. A 6-pack is resting beside it.")
    #Items that I added and made observable in room 4
    r4.addItem("Bar", " The mug is resting on it.")
    r4.addGrabbable("mug")
    
    #set room 1 as the current room at the beginning of the game
    currentRoom = r1

inventory = []
createRooms()


while (True):
    #set the status so user has situational awarness
    status = "{}\nYou are carrying: {}\n".format(currentRoom, inventory)

    #if the current room is None, then the player is dead
    if (currentRoom == None):
        status = "You are dead."
    print "============================="
    print status

    #if the current room is None, exit the game
    if (currentRoom == None):
        death()
        break

    #prompt the player for imput to know what to do
    action = raw_input("What to do?")
    action = action.lower()

    #exit game if the player wants to leave
    if (action == "quit" or action == "exit" or action == "bye"):
        break

    response = "I don't understand. Try verb noun. Valid verbs are go, look, and take"
    words = action.split()

    #the game only understands two word inputs
    if (len(words) == 2):
        verb = words[0]
        noun = words[1]


        #the verb is go
        if (verb == "go"):
            response = "Invalid exit."
            
            if(noun in currentRoom.exits):
                currentRoom = currentRoom.exits[noun]
                response = "Room changed."

            
 
        #the verb is look
        elif (verb == "look"):
            response = "I don't see that item."
            if(noun in currentRoom.items):
                response = currentRoom.items[noun]

        #the verb is take
        elif (verb == "take"):
            response = "I don't see that item."
            
            #check for valid grabbable items in the current room
            for grabbable in currentRoom.grabbables:
                if (noun == grabbable):
                    inventory.append(grabbable)

                    currentRoom.delGrabbable(grabbable)
                    response = "Item grabbed."
                    break
print "\n{}".format(response)
            
        
        
