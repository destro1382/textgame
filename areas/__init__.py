class Room():
    def __init__(self, name, description, exits, items, npcs):
        self.name = name
        self.description = description
        self.exits = exits
        self.items = items
        self.npcs = npcs