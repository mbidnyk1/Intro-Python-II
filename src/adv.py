import textwrap
from room import Room
from player import Player
from item import Item

wrapper = textwrap.TextWrapper(width=50)
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

items = [
    Item("Salamandra", "A fiery sword deadly to all dinosaurs."),
    Item("Black_Pendant", "An ominous glow surrounds this ancient pendant."),
    Item("Brutal_Potion", "Just a drop of this potion can infuse you with maddening strength."),
    Item("Butterfly_Dagger", "An extremely light dagger, with Elma engraved at the hilt."),
]

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
room['outside'].add_item(items[0])
room['foyer'].add_item(items[1])
room['narrow'].add_item(items[2])
player_name = input("What is your name? \n")
player = Player(player_name,"Outside Cave Entrance")
curr_room = room['outside']
action_error = 'Movement not allowed in that direction. **Use keys: [n, s, e, w] for each respective direction**'

def check_item(item_name,loot):
    for item in loot:
        if item == item_name:
            return item.name
    else:
        return False
def print_items(items):
    [print(f'{item}') for item in items]

while True:
    print(f'You arrive at the {player.current_room}')
    wrap_descrip = wrapper.wrap(text=curr_room.description)
    print(f'{wrap_descrip}')
    print_items(curr_room.loot)
    user_input = input('You can move north, south, east, or west. **Use keys: [n, s, e, w] for each respective direction** \n')
    action = user_input.strip().split()
    print(f'{action}')
    if len(action) == 1:
        action = action[0] 
        if action == 'n':
            try: 
            
                curr_room = curr_room.n_to
                player.current_room = curr_room.name
                print(f'You move north')
            except AttributeError: 
                print(action_error)
    
        elif action == 's':
            try: 
                curr_room.s_to
            except AttributeError: 
                print(action_error)
            else:
                curr_room = curr_room.s_to
                player.current_room = curr_room.name
                print(f'You move south')
        elif action == 'e':
            try: 
                curr_room.e_to
            except AttributeError: 
                print(action_error)
            else:
                curr_room = curr_room.e_to
                player.current_room = curr_room.name
                print(f'You move east')
        elif action == 'w':
            try: 
                curr_room.w_to
            except AttributeError: 
                print(action_error)
            else:
                curr_room = curr_room.w_to
                player.current_room = curr_room.name
                print(f'You move west')
        elif action == 'i':
            player.get_inventory()
        elif action == 'q':
            exit()
        else:
            print(action_error)
    elif len(action) == 2:
        if action[0] == 'get' and check_item(action[1], curr_room.loot) != False:
           target_item = check_item(action[1], curr_room.loot)
           curr_room.drop_item(target_item)
           player.add_item(target_item)
           target_item.on_take()
        else: print("That item is nowhere in sight.")
    elif action == 'q':
        exit()
    else:
        print(action_error)
    


