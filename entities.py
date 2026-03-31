


class Enemy():
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage


class Item():
    def __init__(self, name, description, effect, value, sell_value):
        self.name = name
        self.description = description
        self.value = value
        self.sell_value = sell_value
        self.effect = effect
        

       

enemies = {
    "goblin": Enemy("Goblin", 10, 5),
    "skeleton": Enemy("Skeleton", 20, 10),
    "giant rat": Enemy("Giant Rat", 5, 5),
    "orc warrior": Enemy("Orc Warrior", 30, 10),
    "rat man": Enemy("Rat Man", 10, 5),
    "orc lord": Enemy("Orc Lord", 50, 15)
}

items = {
    "short sword": Item("Short Sword", "A surprisingly well preserved steel sword", "damage_boost", 2, 50),
    "breast plate": Item("Breast Plate", "Sturdy enough to deflect a decent blow", "armor_boost", 2, 75),
    "tarnished crown": Item("Tarnished crown", "A tarnished gold crown that gives an ominuous aura", "curse", 3, 100),
    "magic ring": Item("Magic Ring", "A ring that seems to be imbued with a powerful enchantment", "damage_boost", 1, 100),
    "healing potion": Item("Healing Potion", "A surprisingly delicious and invigorating elixer", "healing", 20, 50),
    "shield": Item("Shield", "Not particularly large but it will deflect some incoming damage", "armor_boost", 2, 75),
    "mysterious key": Item("Mysterious Key", "An oddly shaped item that seems to be a key", "open_secret", 1, 5),
    "helm of the mighty": Item("Helm of the Mighty", "A steel helmet that provides decent visibility", "armor_boost", 1, 50),
    "sword of drantill": Item("Sword of Drantill", "The mythical sword of legend", "damage_boost", 5, 1000),
    "grand amulet": Item("Grand Amulet", "An ornate that gives a sense of ease when worn", "armor_boost", 1, 200),
    "test sword": Item("Test Sword", "A remarkably generic sword of testing", "damage_boost", 1, 0)
}
