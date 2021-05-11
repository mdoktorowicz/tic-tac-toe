from map import *

choice_list = ['tl', 't', 'tr', 'l', 'c', 'r', 'bl', 'b', 'br']
choices_made = []
wrong_mark_placement = "You placed a mark incorrectly. Please try again"

def welcome_msg():
    print('''
    888   d8b        888                   888
    888   Y8P        888                   888
    888              888                   888
    888888888 .d8888b888888 8888b.  .d8888b888888 .d88b.  .d88b.
    888   888d88P"   888       "88bd88P"   888   d88""88bd8P  Y8b
    888   888888     888   .d888888888     888   888  88888888888
    Y88b. 888Y88b.   Y88b. 888  888Y88b.   Y88b. Y88..88PY8b.
     "Y888888 "Y8888P "Y888"Y888888 "Y8888P "Y888 "Y88P"  "Y8888
     ''')

def print_game():
    print('Current map:\n')
    print(''.join(top_row))
    print(''.join(divider))
    print(''.join(mid_row))
    print(''.join(divider))
    print(''.join(bot_row))
    print('\n')

def make_choice(counter):
    global choice
    global choices_made

    if counter % 2 == 0:
        player = '1'
    else:
        player = '2'
    
    choice = input(f'''Player {player}'s turn. Where do you want to put a mark? Type:
tl | t | tr
------------
l | c  | r  
------------
bl | b  | br \n\n''').lower()

    if choice not in choice_list:
        print("This isn't a valid choice. Please try again.")
        make_choice(counter)
    elif choice in choices_made:
        print("There's a mark in this field already. Please make another choice.\n")
        make_choice(counter)
    else:
        choices_made.append(choice)


def place_mark(counter):
    global choice
    if counter % 2 == 0:
        mark = 'X'
    else:
        mark = 'O'
    
    if choice == 'tl':
        if not top_row[1] == "X" or top_row[1] == "O":
            top_row[1] = mark
        else:
            print(wrong_mark_placement)
            make_choice(counter)
    elif choice == 't':
        top_row[5] = mark
    elif choice == 'tr':
        top_row[9] = mark
    elif choice == 'l':
        mid_row[1] = mark
    elif choice == 'c':
        mid_row[5] = mark
    elif choice == 'r':
        mid_row[9] = mark
    elif choice == 'bl':
        bot_row[1] = mark
    elif choice == 'b':
        bot_row[5] = mark
    elif choice == 'br':
        bot_row[9] = mark

def check_end_game():
    '''Function returns False if game is over. True otherwise'''

    # Horizontal row win
    if top_row[1] == 'X' and top_row[5] == 'X' and top_row[9] == 'X':
        print("Player 1 won! Game over")
        return False

    elif mid_row[1] == 'X' and mid_row[5] == 'X' and mid_row[9] == 'X':
        print("Player 1 won! Game over")
        return False

    elif bot_row[1] == 'X' and bot_row[5] == 'X' and bot_row[9] == 'X':
        print("Player 1 won! Game over")
        return False

    elif mid_row[1] == 'O' and mid_row[5] == 'O' and mid_row[9] == 'O':
        print("Player 2 won! Game over")
        return False

    elif top_row[1] == 'O' and top_row[5] == 'O' and top_row[9] == 'O':
        print("Player 2 won! Game over")
        return False

    elif bot_row[1] == 'O' and bot_row[5] == 'O' and bot_row[9] == 'O':
        print("Player 2 won! Game over")
        return False

    # Vertical row win

    elif top_row[1] == 'X' and mid_row[1] == 'X' and bot_row[1] == 'X':
        print("Player 1 won! Game over")
        return False

    elif top_row[5] == 'X' and mid_row[5] == 'X' and bot_row[5] == 'X':
        print("Player 1 won! Game over")
        return False

    elif top_row[9] == 'X' and mid_row[9] == 'X' and bot_row[9] == 'X':
        print("Player 1 won! Game over")
        return False

    elif top_row[1] == 'O' and mid_row[1] == 'O' and bot_row[1] == 'O':
        print("Player 2 won! Game over")
        return False

    elif top_row[5] == 'O' and mid_row[5] == 'O' and bot_row[5] == 'O':
        print("Player 2 won! Game over")
        return False

    elif top_row[9] == 'O' and mid_row[9] == 'O' and bot_row[9] == 'O':
        print("Player 2 won! Game over")
        return False

    # Diagonal win

    elif top_row[1] == 'X' and mid_row[5] == 'X' and bot_row[9] == 'X':
        print("Player 1 won! Game over")
        return False

    elif top_row[9] == 'X' and mid_row[5] == 'X' and bot_row[1] == 'X':
        print("Player 1 won! Game over")
        return False

    elif top_row[1] == 'O' and mid_row[5] == 'O' and bot_row[9] == 'O':
        print("Player 2 won! Game over")
        return False

    elif top_row[9] == 'O' and mid_row[5] == 'O' and bot_row[1] == 'O':
        print("Player 2 won! Game over")
        return False

    else:
        return True