import Item

class Consumables(Item):
    def __init__(self, health):
        super().__init__(self)
        self.health = health
