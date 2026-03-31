from rooms.py import Room

village_entrance = Room(
    "Village Entrance",
    "You find yourself at the entryway of a dark and foreboding keep.  As the sky darkens overhead, the ominous feeling in your breast grows dramatically.\nDespite this feeling, you know that your quest lies within these walls. You must enter and face what is within.\nThe only way forward is through the grand doors ahead to the South.",
    {"south": "entrance", "north": "village square"},
    [],
    []
)

village_square = Room(
    "Village square",
    "You find yourself at the entryway of a dark and foreboding keep.  As the sky darkens overhead, the ominous feeling in your breast grows dramatically.\nDespite this feeling, you know that your quest lies within these walls. You must enter and face what is within.\nThe only way forward is through the grand doors ahead to the South.",
    {"south": "village entrance", "north": "northern village", "east": "blacksmith", "west": "inn"},
    [],
    []
)