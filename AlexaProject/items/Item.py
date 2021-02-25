# Here is where the top abstract item class will go

class Item():
    def __init__(self, name, item_type, traits={}):
        self.name = name #type: str
        self.item_type = item_type #type: str
        self.traits = traits
