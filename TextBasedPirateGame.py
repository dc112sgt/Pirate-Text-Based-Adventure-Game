def show_instructions():
    # print a main menu and commands
    print('Pirate Text Adventure Game')
    print('Collect 6 items to win the game, or fail your mission.')
    print('Move commands: go South, go North, go East, go West')
    print("Add to Inventory: get 'item name'")


def show_status():
    print("You are currently in {}".format(current_island))
    current_dict = islands[current_island]
    item = 'None'
    if 'item' in current_dict:
        item = current_dict['item']
    print('Item in this room:', item)
    print("Inventory:", inventory)


# define inventory which begins empty
islands = {
    'Isla Blanquilla': {'South': 'Cumana', 'East': 'Grenada', 'West': 'Curacao', 'North': 'St. Kitts'},
    'Curacao': {'East': 'Isla Blanquilla', 'item': 'Cutlass'},
    'Grenada': {'West': 'Isla Blanquilla', 'North': 'Barbados', 'item': 'Cannons'},
    'Barbados': {'South': 'Grenada', 'item': 'Treasure Ship'},
    'St. Kitts': {'South': 'Isla Blanquilla', 'East': 'Antigua', 'item': 'Crew'},
    'Antigua': {'West': 'St. Kitts', 'item': 'Frigate'},
    'Cumana': {'North': 'Isla Blanquilla', 'East': 'Trinidad', 'item': 'Gold Doubloons'},
    'Trinidad': {'West': 'Cumana', 'item': 'Rum'}
}

inventory = []

starting_island = 'Isla Blanquilla'

current_island = starting_island

show_instructions()

while True:
    show_status()

    if current_island == 'Barbados':
        # check number of items
        print('You reach the final room')
        if len(inventory) == 6:
            print('You win!')
        else:
            print('You lose!')
        break  # end game

    # prompt user to input compass heading
    word_list = input("Enter 'Go North, South, East, West' to sail or 'Exit' to exit game: ").split()
    word_list = [x.capitalize() for x in word_list]
    if len(word_list) == 1:
        if word_list[0] == "Exit":
            current_island = 'exit'
            break
        else:
            print('Invalid input')
            continue
    elif len(word_list) >= 2:
        action = word_list[0]

        if action == "Go":
            # ensure we have only two words
            if len(word_list) > 2:
                print('Invalid input.')
                continue
            direction = word_list[1]
            possible_islands = islands[current_island]
            if direction in possible_islands:
                current_island = possible_islands[direction]
            else:
                print(f'Could not go to {direction} from {current_island}.')
        elif action == "Get":
            if 'item' in islands[current_island]:
                # item name combines all the words after the first word
                item_name = ''
                i = 1
                for val in word_list[1:]:
                    if i != 1:
                        item_name += f' {val}'
                    else:
                        item_name += val
                    i += 1
                if islands[current_island]["item"] == item_name:
                    inventory.append(item_name)
                    islands[current_island].pop("item")
                    # check for end game
                    if len(inventory) == 6:
                       print('You collected all the items. You won')
                       break
                else:
                    print("This item is not in this room")
            else:
                print("There is no item here")

        else:
            print('Invalid action.')
    else:
        print('Invalid input')