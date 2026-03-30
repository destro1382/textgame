#Imports
from entities import Enemy, Item, enemies, items
#Rooom Class
class Room():
    def __init__(self, name, description, exits, items, npcs):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = items
        self.npcs = npcs


entrance_room = Room(
    "Entrance",
    "You find yourself at the entryway of a dark and foreboding keep.  As the sky darkens overhead, the ominous feeling in your breast grows dramatically.\nDespite this feeling, you know that your quest lies within these walls. You must enter and face what is within.\nThe only way forward is through the grand doors ahead to the South.",
    {"south": "hall 1"},
    [],
    []
)

hallway_room_1 = Room(
    "Hall 1",
    "As you enter the keep, you find yourself in a long and dimly lit hallway that slopes downward. The walls are adorned with faded tapestries.\nOnce this was clearly a place of grand opulence. However, it now seems to have faded to nothing more than a forgotten memory.\nThe smell immediately hits you of rot and stale air.\nIn front of you to the South is a door with a faint light flickering beneath.",
    {"north": "entrance",  "south": "audience chamber"},
    ["Torch"],
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
    ["Short Sword", "Breast Plate"],
    [enemies["goblin"]]
)

audience_chamber = Room(
    "Audience Chamber",
    "Past the doorway is a room that seems like it was once a greeting area for visiting guests.\nThe halls are adorned with similar tapestries to those you have already seen. They depict scenes of regal lords ruling over the land.\nThere are several tables that have broken and decayed over the years with a small throne sitting in the south east corner.\nThere are exits to North, South, East, and West.",
    {"north": "hall 1", "east": "hall 3", "south": "hall 6", "west": "hall 2"},
    ["Tarnished Crown"],
    []
)

dining_room = Room(
    "Dining Room",
    "It is clear that this room was once a dining hall. The ornate carvings are still observable from the severely rotted wood that remains.\nThere are still shards of broken plates on the floor, not worthy of the goblins looting no doubt.\nThere must have been much evil that ocurred here.\nThe exits are to the East, West, and South.",
    {"west": "hall 3", "east": "hall 4", "south": "hall 7"},
    ["Magic Ring"],
    [enemies["skeleton"]]
)

servants_area = Room(
    "Servants Area",
    "No grandeur exists within this room. It is clear this is where the servants lived, prepared meals and washed for the rulers of the keep.\nSomehow even now, it feels inferior to the other chambers.\nThe only exit is to the West.",
    {"west": "dining room"},
    ["Healing Potion"],
    [Enemy("Giant Rat", 5, 5)]
)

#Barracks
barracks = Room(
    "Barracks",
    "You come to what was clearly the barracks for the keep guard. The cramped quarters still would have held place for a dozen or so guards.\nNow all that remains are broken bunks and blood stains. Perhaps these soldiers met with an untimely end.\nThe only exit is to the North.",
    {"north": "hall 5"},
    ["Shield"],
    [Enemy("Orc Warrior", 30, 10)]
)

#SecretRoom
secret_room = Room(
    "Secret Room",
    "As you pass behind the tapestry you find yourself in a small room with several rotting skeletons within.\nThis would seem to be a secret room to hide from intruders, unfortunately it seems to have worked too well.\nExit to the East",
    {"east": "guest quarters"},
    ["Mysterious Key", "Health Potion", "Helm of the Mighty"],
    []
)

#Guest Quarters
guest_quarters = Room(
    "Guest Quarters",
    "These would seem to be the guest quarters. While they lack some of thet regal feel of the rest of the keep.\nThe opulence still outshines any where of the surrounding lands you have seen despite the rotted and deserted nature.\nExits to the West and North",
    {"west": "secret room", "north": "hall 6"},
    ["Health Potion"],
    [Enemy("Rat man", 10, 5)]
)
#Throne Room
throne_room = Room(
    "Throne Room",
    "Clearly this is where the lord sat and held court. Within this room, you first notice a massive poorly constructed chair where once sat a mighty throne.\nThe throne itself has clearly been stripped of any ornamentation and now sits discarded.\nExits to the North and West",
    {"north": "hall 7", "west": "hall 8"},
    ["Sword of Drantill"],
    [Enemy("Orc Lord", 50, 15)]
)
#Royal Chambers
royal_chambers = Room(
    "Royal Chambers",
    "The bedchambers of the lord and lady clearly. There is a massive broken bedframe, blood covers every wall.\nThis was perhaps once a place of peaceful relaxation but has been turned into a place of horror.\n Exit to the East",
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
    "servants area": servants_area,
    "barracks": barracks,
    "secret room": secret_room,
    "guest quarters": guest_quarters,
    "throne room": throne_room,
    "royal chambers": royal_chambers
   
}
