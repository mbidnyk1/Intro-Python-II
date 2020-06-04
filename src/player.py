# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []
    def add_item(self,item):
        self.inventory.append(item)
    def drop_item(self,item):
        self.inventory.remove(item)
    def get_inventory(self):
        [print(f'{item.__str__()}') for item in self.inventory]
    def __str__(self):
        return f"Player: {self.name}"
    def __repr__(self):
        return f"Player({repr(self.name)})"

# class Inventory(Player):
#     def __init__(self, items):
#         self.items = items
#     def __str__(self):
#         return f"Inventory: {self.items}"
#     def __repr__(self):
#         return f"Inventory({repr(self.items)})"