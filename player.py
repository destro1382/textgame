#Import
from rooms import all_rooms

#Player Class
class Player():
    #Player Constructor
    def __init__(self, name, health, damage, inventory, current_room):
        self.name = name
        self.health = health
        self.damage = damage
        self.inventory = inventory
        self.current_room = current_room
    #Stat Display
    def disp_stats(self):
        print(f"{self.name} has {self.health} health points.")
        print(f"{self.name} has the following items in their inventory: {', '.join(self.inventory)}.")
    #Player Move
    def move(self, direction):
        #Checks if moving direction is in exits from current room
        if direction in self.current_room.exits:
            #Sets variable of room to travel to be the room tied to the direction typed
            new_room_name = self.current_room.exits[direction]
            #Resets the current room on player to the new room
            self.current_room = all_rooms[new_room_name]
            print(f"You move {direction} to the {self.current_room.name}.")
            print(self.current_room.description)
        else:
            print("You can't go that way.")
    #Player Search
    def search(self):
        if self.current_room.items == []:
            print("You search the room but find nothing of interest.")
        else:
            print("You search the room and find the following items:")
            for item in self.current_room.items:
                print(f" - {item}, you add it to your inventory.")
                self.inventory.append(item)
                self.current_room.items.remove(item)