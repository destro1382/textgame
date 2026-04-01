#Import
from areas.world import all_rooms


#Player Class
class Player():
    #Player Constructor
    def __init__(self, name, health, damage, armor, inventory, current_room):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self.inventory = inventory
        self.current_room = current_room
    #Stat Display
    
    def disp_stats(self):
        print(f"{self.name} has {self.health} health points.")
        print(f"{self.name} does {self.damage} damage.")
        print(f"{self.name} is protected by {self.armor} points of armor.")
        print(f"{self.name} has the following items in their inventory:")
        for item in self.inventory:
            print(f" - {item.name}")
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
                print(f" - {item.name}, you add it to your inventory.")
                self.inventory.append(item)
                self.current_room.items.remove(item)
                self.update_stats(item)
    
    def update_stats(self, item):
        if item.effect == "damage_boost":
            self.damage += item.value
        elif item.effect == "armor_boost":
            self.armor += item.value