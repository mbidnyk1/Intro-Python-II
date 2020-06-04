class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    def on_take(self):
        return print(f"You have picked up {str(self.name)}.")
    def __str__(self):
        return f'{self.name}'
    # def __repr__(self):
    #     return f"{repr(self.name)}"