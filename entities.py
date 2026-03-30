


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


enemies = {
    "goblin": Enemy("Goblin", 10, 5)
}

items = {}
