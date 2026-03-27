

class Room():
    def __init__(self, name, description, exits):
        self.name = name
        self.description = description
        self.exits = exits


entrance_room = Room(
    "Entrance",
    "You are standing at the entrance of a dark and ominous castle. The air is thick with the scent of decay and danger. The only way forward is through the grand doors ahead.",
    {"south": "hallway"}
)

hallway_room = Room(
    "Hallway",
    "You find yourself in a long, dimly lit hallway. The walls are adorned with faded tapestries, and the floor is covered in dust. You can hear faint whispers echoing through the air. There are doors to the north, east, and west.",
    {"north": "entrance", "east": "armory", "south": "library"}
)
armory_room = Room(
    "Armory",
    "You enter a room filled with ancient weapons and armor. The shelves are lined with swords, shields, and suits of armor. The air is heavy with the scent of rust and metal. There is a door to the west.",
    {"west": "hallway"}
)   
library_room = Room(
    "Library",
    "You step into a grand library filled with towering bookshelves. The air is thick with the scent of old paper and leather. The shelves are filled with dusty tomes and ancient scrolls. There is a door to the north.",
    {"north": "hallway", "east": "lair"}
)
lair_room = Room(
    "Lair",
    "You enter a dark and foreboding lair. The air is thick with the scent of decay and danger. The walls are adorned with grotesque tapestries, and the floor is covered in bloodstains. You can hear the sound of something breathing in the darkness. There is a door to the west.",
    {"west": "library"}
)

all_rooms = {
    "entrance": entrance_room,
    "hallway": hallway_room,
    "armory": armory_room,
    "library": library_room,
    "lair": lair_room
}
