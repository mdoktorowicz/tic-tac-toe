from map import *
from game_logic import *

move_counter = 0
game_ongoing = True

welcome_msg()

while game_ongoing:
    make_choice(move_counter)
    place_mark(move_counter)
    move_counter += 1

    print_game()
    if not check_end_game():
        game_ongoing = False

    if move_counter == 9 and check_end_game():
        print("Game over! It's a draw")
        game_ongoing = False