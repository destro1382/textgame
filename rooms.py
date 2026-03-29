from entities import Enemy, Items
class Room():
    def __init__(self, name, description, exits, items, npcs):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = items
        self.npcs = npcs


entrance_room = Room(
    "Entrance",
    "You find yourself at the entryway of a dark and foreboding keep.  As the sky darkens overhead, the ominous feeling in your breast grows dramatically. Despite this feeling, you know that your quest lies within these walls. You must enter and face what is within. The only way forward is through the grand doors ahead to the south.",
    {"south": "hall 1"},
    [],
    []
)

hallway_room_1 = Room(
    "Hall 1",
    "As you enter the keep, you find yourself in a long and dimly lit hallway that slopes downward. The walls are adorned with faded tapestries. Once this was clearly a place of grand opulence. However, it now seems to have faded to nothing more than a forgotten memory. The smell immediately hits you of rot and stale air. In front of you to the south is a door with a faint light flickering beneath.",
    {"north": "entrance",  "south": "audience chamber"},
    ["torch"],
    [] 
)


hallway_room_2 = Room(
    "Hall 2",
    "Another hallway, adorned with the same types of tapestries that are becoming familiar. There are doorways to the east and west.",
    {"west": "armory", "east": "audience chamber"},
    [],
    [] 
)


hallway_room_3 = Room(
    "Hall 3",
    "Another hallway, adorned with the same types of tapestries that are becoming familiar. There are doorways to the east and west.",
    {"west": "audience chamber", "east": "dining room"},
    [],
    [] 
)


hallway_room_4 = Room(
    "Hall 4",
    "Another hallway, adorned with the same types of tapestries that are becoming familiar. There are doorways to the east and west.",
    {"west": "dining room", "east": "servants area"},
    [],
    [] 
)

hallway_room_5 = Room(
    "Hall 5",
    "Another hallway, adorned with the same types of tapestries that are becoming familiar. There are doorways to the east and west.",
    {"north": "armory", "south": "barracks"},
    [],
    [] 
)

hallway_room_6 = Room(
    "Hall 6",
    "Another hallway, adorned with the same types of tapestries that are becoming familiar. There are doorways to the east and west.",
    {"north": "audience chamber", "south": "guest quarters"},
    [],
    [] 
)

hallway_room_7 = Room(
    "Hall 7",
    "Another hallway, adorned with the same types of tapestries that are becoming familiar. There are doorways to the east and west.",
    {"north": "dining room", "south": "throne room"},
    [],
    [] 
)

hallway_room_8 = Room(
    "Hall 8",
    "Another hallway, adorned with the same types of tapestries that are becoming familiar. There are doorways to the east and west.",
    {"west": "royal chambers", "east": "throne room"},
    [],
    [] 
)

armory_room = Room(
    "Armory",
    "As you enter, it is quite clear this used to be an armory. Racks of swords, shields, spears and armor. The grand majority is rusted beyond any use. However there may be a piece or two that are of some use. Skulking in the corner is a short goblin armed with a rusty short sword.",
    {"east": "hall 2"},
    ["short sword", "breast plate"],
    [Enemy("Goblin", 30, 5)]
)

audience_chamber = Room(
    "Audience Chamber",
    "Past the doorway is a room that seems like it was once a greeting area for visiting guests. The halls are adorned with similar tapestries to those you have already seen. They depict scenes of regal lords ruling over the land. There are several tables that have broken and decayed over the years with a small throne sitting in the south east corner. There are exits to north, south, east, and west.",
    {"north": "hall 1", "east": "hall 3", "south": "hall 6", "west": "hall 2"},
    ["tarnished crown"],
    []
)

dining_room = Room(
    "Dining Room",
    "It is clear that this room was once a dining hall. The ornate carvings are still observable from the severely rotted wood that remains. There are still shards of broken plates on the floor, not worthy of the goblins looting no doubt. There must have been much evil that ocurred here. Indeed it appears some of it is rising right now...  The exits are to the east, west, and south."
    #"You step into a grand library filled with towering bookshelves. The air is thick with the scent of old paper and leather. The shelves are filled with dusty tomes and ancient scrolls. There is a door to the north, and a large and imposing door to the east.",
    {"west": "hall 3", "east": "hall 4", "south": "hall 7"},
    ["magic ring"],
    [Enemy("Skeleton", 20, 10)]
)
#Servants area
#Barracks
#SecretRoom
#Guest Quarters
#Throne Room
#Royal Chambers


#Needs editing
library_room = Room(
    "Library",
    "You step into a grand library filled with towering bookshelves. The air is thick with the scent of old paper and leather. The shelves are filled with dusty tomes and ancient scrolls. There is a door to the north, and a large and imposing door to the east.",
    {"north": "hallway", "east": "lair"},
    [],
    [Enemy("Skeleton", 20, 10)]
)

#Needs editing
lair_room = Room(
    "Lair",
    "You enter a dark and foreboding lair. The air is thick with the scent of decay and danger. The walls are adorned with grotesque tapestries, and the floor is covered in bloodstains. You can hear the sound of something breathing in the darkness. There is a door to the west.",
    {"west": "library"},
    ["Sword of Drantill"],
    [Enemy("Orc Lord", 50, 15)]
)

all_rooms = {
    "entrance": entrance_room,
    "hall 1": hallway_room_1,
    "hall 2": hallway_room_2,
    "hall 3": hallway_room_3,
    "hall 4": hallway_room_4,
    "hall 5": hallway_room_5,
    "hall 6": hallway_room_6,
    "hall 7": hallway_room_7,
    "hall 8": hallway_room_8,
    "audience chamber": audience_chamber,
    "armory": armory_room,
    "library": library_room,
    "lair": lair_room
}
