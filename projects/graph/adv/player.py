class Player:
    def __init__(self, name, startingRoom, startingItems=[]):
        self.name = name
        self.currentRoom = startingRoom
        self.items = startingItems
    def travel(self, direction):
        nextRoom = self.currentRoom.getRoomInDirection(direction)
        if nextRoom is not None:
            self.currentRoom = nextRoom
            nextRoom.printRoomDescription(self)
        else:
            print("You cannot move in that direction.")
    def look(self, direction=None):
        if direction is None:
            self.currentRoom.printRoomDescription(self)
        else:
            nextRoom = self.currentRoom.getRoomInDirection(direction)
            if nextRoom is not None:
                nextRoom.printRoomDescription(self)
            else:
                print("There is nothing there.")
    def printStatus(self):
        print(f"Your name is {self.name}")
    def printInventory(self):
        print("You are carrying:\n")
        for item in self.items:
            print(f"  {item.name} - {item.description}\n")
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        self.items.remove(item)
    def findItemByName(self, name):
        for item in self.items:
            if item.name.lower() == name.lower():
                return item
        return None
    def dropItem(self, itemName):
        itemToDrop = self.findItemByName(" ".join(itemName))
        if itemToDrop is not None:
            self.removeItem(itemToDrop)
            self.currentRoom.addItem(itemToDrop)
            itemToDrop.on_drop()
        else:
            print("You are not holding that item.")
    def findPathToItem(self, item):
        
        stack = [self.currentRoom]
        previous_room = None
        while(len(stack) > 0):
            print(len(stack))
            current_room = stack.pop()
            print(current_room.name)
            if(item in current_room.items):
                print(f"Treasure at {current_room.name}")
                return
            directions = current_room.getPossibleDirections(True)
            for direction in directions:
                neighbor = getattr(current_room, direction)
                if neighbor != previous_room:
                    stack.append(neighbor)
            previous_room = current_room
        print("No treasure")


