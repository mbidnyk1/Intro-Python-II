# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.loot = []
    def add_items(self,item):
        self.loot.append(item)
    def get_description(self):
        return {self.description}
    def __str__(self):
        return f"Room: {self.name}, {self.description}"
    def __repr__(self):
        return f"Room({repr(self.name)}, {repr(self.description)}"

# class Loot(Room):
#     def __init__(self,items): 
#         self.items = items
#     def __str__(self):
#         return f"Loot: {self.items}"
#     def __repr__(self):
#         return f"Loot({repr(self.items)})"

