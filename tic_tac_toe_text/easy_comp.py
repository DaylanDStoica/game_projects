from random import randint 
# from tic_tac_toe import empty_spot, player1, player2
# from header import empty_spot, player1, player2
import header as h
def comp_decide(the_board):
    # given a 3x3 tic tac toe board 
    # randomly choose an open space to place a piece
    pass 

def check_space_for_empty ( the_board, x_guess, y_guess):
    # return True if the given coords are empty
    # return False otherwise
    chosen_spot = the_board[y_guess][x_guess]
    # if chosen_spot==player1 or chosen_spot==player2:
    #     return False 
    # else: 
    #     return True 
    if chosen_spot == h.empty_spot:
        return True 
    else:
        return False