class Enemy():
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage


class Item():
    def __init__(self, name, description):
        self.name = name
        self.description = description