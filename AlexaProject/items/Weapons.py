import Item

class Weapons(Item):
    def __init__(self, durability, damage):
        super().__init__(self)
        self.durability = durability
        self.damage = damage
            
