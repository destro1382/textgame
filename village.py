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

blacksmith = Room(
    "Blacksmith",
    "You find yourself at the entryway of a dark and foreboding keep.  As the sky darkens overhead, the ominous feeling in your breast grows dramatically.\nDespite this feeling, you know that your quest lies within these walls. You must enter and face what is within.\nThe only way forward is through the grand doors ahead to the South.",
    {"west": "village square"},
    [],
    []
)

inn = Room(
    "inn",
    "You find yourself at the entryway of a dark and foreboding keep.  As the sky darkens overhead, the ominous feeling in your breast grows dramatically.\nDespite this feeling, you know that your quest lies within these walls. You must enter and face what is within.\nThe only way forward is through the grand doors ahead to the South.",
    {"east": "village square"},
    [],
    []
)

northern_village = Room(
    "Northern Village",
    "You find yourself at the entryway of a dark and foreboding keep.  As the sky darkens overhead, the ominous feeling in your breast grows dramatically.\nDespite this feeling, you know that your quest lies within these walls. You must enter and face what is within.\nThe only way forward is through the grand doors ahead to the South.",
    {"south": "village square"},
    [],
    []
)