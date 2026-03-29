from rooms import all_rooms
class Player():
    def __init__(self, name, health, damage, inventory, current_room):
        self.name = name
        self.health = health
        self.damage = damage
        self.inventory = inventory
        self.current_room = current_room

    def disp_stats(self):
        print(f"{self.name} has {self.health} health points.")
        print(f"{self.name} has the following items in their inventory: {', '.join(self.inventory)}.")

    def move(self, direction):
        if direction in self.current_room.exits:
            new_room_name = self.current_room.exits[direction]
            self.current_room = all_rooms[new_room_name]
            print(f"You move {direction} to the {self.current_room.name}.")
            print(self.current_room.description)
        else:
            print("You can't go that way.")

    def search(self):
        if self.current_room.items == []:
            print("You search the room but find nothing of interest.")
        else:
            print("You search the room and find the following items:")
            for item in self.current_room.items:
                print(f" - {item}, you add it to your inventory.")
                self.inventory.append(item)
                self.current_room.items.remove(item)