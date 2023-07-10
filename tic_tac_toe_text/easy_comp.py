from random import randint
# from tabnanny import check
# from tkinter import Y 
# from tic_tac_toe import empty_spot, player1, player2
# from header import empty_spot, player1, player2
# import header as h
# from . import my_header as h
import my_header as h
def comp_decide(the_board):
    # given a 3x3 tic tac toe board 
    # randomly choose an open space to place a piece
    not_yet_placed = True 
    # as long as an empty spot is not yet found, continue generating coordinates 
    while not_yet_placed: 
        y_guess = randint(1,3)
        x_guess = randint(1,3)
        print("computer checking spot: (", x_guess, ",", y_guess, ")...")
        check_result = check_space_for_empty(the_board, x_guess= x_guess-1, y_guess= y_guess-1)
        if check_result: # the generated coords contain an empty spot 
            # the_board[y_guess-1][x_guess-1] = h.player2 # this line writes to columns, not elements
            # the_board[y_guess-1][x_guess-1] = h.player2
            # print(the_board)
            not_yet_placed = False  # a spot has now been placed.
            break
    the_board[y_guess-1][x_guess-1] = h.player2 # this line writes to columns, not elements

# TODO: solve the bug of 'filling up an entire column'
def check_space_for_empty ( the_board, x_guess=0, y_guess=0):
    # return True if the given coords are empty
    # return False otherwise
    chosen_spot = the_board[y_guess][x_guess]
    # if chosen_spot==player1 or chosen_spot==player2:
    #     return False 
    # else: 
    #     return True 
    if chosen_spot == h.empty_spot: # the given spot is empty
        print("   spot ( %1d, %1d) is an empty spot" % (x_guess, y_guess) )
        # print( chosen_spot)
        return True 

    else:
        return False