#Memory Game
import os
import random
import time

num_rows = 4
num_cols = 5


if (num_rows * num_cols) % 2 != 0:
    raise ValueError("There must be an even number of spots.")


hidden_card = "#"
empty_spot = " "
delay = 2 #time in seconds cards revealed for


def clear():
    os.sytem ("cls" if os.name == "nt" else "clear")


def print_title():
    print (r'    MEMORY GAME  ')


def print_instructions():   
    print ("Uncover two cards which you think contain the same symbol.")
    print ("Try to find all the pairs in the minimum number of turns.")
    print ()


def play_again():
    print()
    print("Would you like to play again? (yes or no)?")
    return input().lower() .startswith("y")


def create_board():
    cards = []
    for offset in range ((num_rows * num_cols) //2):
        cards.append(chr(65 + offset))

    cards.extend(cards)
    random.shuffle(cards)

    board = []
    for row_num in range (num_rows):
        new_row =[]
        for col_num in range (num_cols):
            new_row.append (cards [row_num * num_cols + col_num])
        board.append(new_row)
    return board


def dispay_cards (board, visible=None):
    if visible is None:
        visible = []
    
    for row_num in range (num_rows):
        for col_num in range (num_cols):
            if (row_num,col_num) in visible:
                print(board[row_num][col_num], end="\t")
            elif board [row_num][col_num] == empty_spot:
                print(empty_spot, end="\t")
            else:
                print(hidden_card, end="\t")
        print()
    print()

def validate_user_input (player_choice, board):
    return True

def get_player_choices(board):
    return [(0,0),(2,0)] # hard coded for testing

def player_turn (board,player_score, player_turns):
    clear()
    print_title()
    print("Turns Taken: ",player_turn)
    print("Current Score: ",player_score)
    print()
    display_cards(board)
    player_choices =get_player_choices(board)
    card1_pos, card2_pos = player_choices
    clear()
    print_title()
    print_instructions()
    print()
    print()
    display_cards(board,player_choices)


def main():
    board = create_board()
    player_turns = 0
    player_score = 0
    success = player_turn(board,player_score,player_turn)

if __name__ == "__main__":
    main()

