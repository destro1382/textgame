from entities import Enemy, Item 
class Room():
    def __init__(self, name, description, exits, items, npcs):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = items
        self.npcs = npcs


entrance_room = Room(
    "Entrance",
    "You find yourself at the entryway of a dark and foreboding keep.  As the sky darkens overhead, the ominous feeling in your breast grows dramatically.\nDespite this feeling, you know that your quest lies within these walls. You must enter and face what is within.\nThe only way forward is through the grand doors ahead to the south.",
    {"south": "hall 1"},
    [],
    []
)

hallway_room_1 = Room(
    "Hall 1",
    "As you enter the keep, you find yourself in a long and dimly lit hallway that slopes downward. The walls are adorned with faded tapestries.\nOnce this was clearly a place of grand opulence. However, it now seems to have faded to nothing more than a forgotten memory.\nThe smell immediately hits you of rot and stale air.\nIn front of you to the south is a door with a faint light flickering beneath.",
    {"north": "entrance",  "south": "audience chamber"},
    ["torch"],
    [] 
)


hallway_room_2 = Room(
    "Hall 2",
    "Another hallway, adorned with the same types of tapestries that are becoming familiar.\nThere are doorways to the East and West.",
    {"west": "armory", "east": "audience chamber"},
    [],
    [] 
)


hallway_room_3 = Room(
    "Hall 3",
    "Another hallway, adorned with the same types of tapestries that are becoming familiar.\nThere are doorways to the East and West.",
    {"west": "audience chamber", "east": "dining room"},
    [],
    [] 
)


hallway_room_4 = Room(
    "Hall 4",
    "Another hallway, adorned with the same types of tapestries that are becoming familiar.\nThere are doorways to the East and West.",
    {"west": "dining room", "east": "servants area"},
    [],
    [] 
)

hallway_room_5 = Room(
    "Hall 5",
    "Another hallway, adorned with the same types of tapestries that are becoming familiar.\nThere are doorways to the North and South.",
    {"north": "armory", "south": "barracks"},
    [],
    [] 
)

hallway_room_6 = Room(
    "Hall 6",
    "Another hallway, adorned with the same types of tapestries that are becoming familiar.\nThere are doorways to the North and South.",
    {"north": "audience chamber", "south": "guest quarters"},
    [],
    [] 
)

hallway_room_7 = Room(
    "Hall 7",
    "Another hallway, adorned with the same types of tapestries that are becoming familiar.\nThere are doorways to the North and South.",
    {"north": "dining room", "south": "throne room"},
    [],
    [] 
)

hallway_room_8 = Room(
    "Hall 8",
    "Another hallway, adorned with the same types of tapestries that are becoming familiar.\nThere are doorways to the East and West.",
    {"west": "royal chambers", "east": "throne room"},
    [],
    [] 
)

armory_room = Room(
    "Armory",
    "As you enter, it is quite clear this used to be an armory. Racks of swords, shields, spears and armor.\nThe grand majority is rusted beyond any use. However there may be a piece or two that are of some use.\nThere are exits to the East and South",
    {"east": "hall 2", "south": "hall 5"},
    ["short sword", "breast plate"],
    [Enemy("Goblin", 30, 5)]
)

audience_chamber = Room(
    "Audience Chamber",
    "Past the doorway is a room that seems like it was once a greeting area for visiting guests.\nThe halls are adorned with similar tapestries to those you have already seen. They depict scenes of regal lords ruling over the land.\nThere are several tables that have broken and decayed over the years with a small throne sitting in the south east corner.\nThere are exits to North, South, East, and West.",
    {"north": "hall 1", "east": "hall 3", "south": "hall 6", "west": "hall 2"},
    ["tarnished crown"],
    []
)

dining_room = Room(
    "Dining Room",
    "It is clear that this room was once a dining hall. The ornate carvings are still observable from the severely rotted wood that remains.\nThere are still shards of broken plates on the floor, not worthy of the goblins looting no doubt.\nThere must have been much evil that ocurred here.\nThe exits are to the East, West, and South.",
    {"west": "hall 3", "east": "hall 4", "south": "hall 7"},
    ["magic ring"],
    [Enemy("Skeleton", 20, 10)]
)

servants_area = Room(
    "Servants Area",
    "No grandeur exists within this room. It is clear this is where the servants lived, prepared meals and washed for the rulers of the keep.\nSomehow even now, it feels inferior to the other chambers.\nThe only exit is to the West.",
    {"west": "dining room"},
    ["healing potion"],
    [Enemy("Giant Rat", 5, 5)]
)

#Barracks
barracks = Room(
    "Barracks",
    "You come to what was clearly the barracks for the keep guard. They certainly packed them in tight.\nThe only exit is to the North.",
    {"north": "hall 5"},
    ["shield"],
    [Enemy("Orc Warrior", 30, 10)]
)

#SecretRoom
secret_room = Room(
    "Secret Room",
    "Secret room, Exit to the East",
    {"east": "guest quarters"},
    ["mysterious key", "health potion", "helm of the mighty"],
    []
)

#Guest Quarters
guest_quarters = Room(
    "Guest Quarters",
    "Guest Quarters, Exits to the West and North",
    {"west": "secret room", "north": "hall 6"},
    ["health potion"],
    [Enemy("Rat man", 10, 5)]
)
#Throne Room
throne_room = Room(
    "Throne Room",
    "Throne room, Exits to the North and West",
    {"north": "hall 7", "west": "hall 8"},
    ["Sword of Drantill"],
    [Enemy("Orc Lord", 50, 15)]
)
#Royal Chambers
royal_chambers = Room(
    "Royal Chambers",
    "Royal chambers, Exit to the East",
    {"east": "hall 8"},
    ["Grand Amulet"],
    []
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
