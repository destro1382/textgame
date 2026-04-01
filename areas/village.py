from areas.__init__ import Room

village_entrance = Room(
    "Village Entrance",
    "Village entrance\nThe village lies to the North, the path to the keep lies to the South.",
    {"south": "entrance", "north": "village square"},
    [],
    []
)

village_square = Room(
    "Village square",
    "Village square\nThe entrance to the village lies to the south, to the North is the northern part of the village,\nTo the East lies the Blacksmith, To the west lies the Inn",
    {"south": "village entrance", "north": "northern village", "east": "blacksmith", "west": "inn"},
    [],
    []
)

blacksmith = Room(
    "Blacksmith",
    "Blacksmith.\nTo the West lies the Village Square",
    {"west": "village square"},
    [],
    []
)

inn = Room(
    "inn",
    "Inn.\nTo the East lies the Village Square",
    {"east": "village square"},
    [],
    []
)

northern_village = Room(
    "Northern Village",
    "Northern Village.\nTo the South lies the Village Square",
    {"south": "village square"},
    [],
    []
)

village_rooms = {
    "village entrance": village_entrance,
    "village square": village_square,
    "blacksmith": blacksmith,
    "inn": inn,
    "northern village": northern_village
}