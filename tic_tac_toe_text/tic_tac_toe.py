
# empty_spot = ''
# player1 = 'X'
# player2 = 'O'
# from header import empty_spot, player1, player2
import my_header as h

# the_grid = [ [h.empty_spot]*3] * 3 # 3x3 grid 
emp_spot = h.empty_spot
# the_grid = [3][3]
# for i in range(0,3):
    # for j in range(0,3):
        # the_grid[i][j] = emp_spot
the_grid = [ [emp_spot]*3 for i in range(3)]
def print_board():
    for y in range(len(the_grid)):
        for x in range(len(the_grid[y])):
            print('|', the_grid[y][x], end = ' ')
        print()
        print( '-'*10)
        

print_board()

def player_turn():
    # take 2 integer inputs from user, the row, and the column

    print(" please give 2 integers for your spot (1-3), (x, y):  ", end='')
    input1 = input().split()
    x = int(input1[0])
    y = int(input1[1])

    the_grid[y-1][x-1] = h.player1
    print_board()

import easy_comp as ec 
def comp_turn():
    # use the decision algorithm from the chosen difficulty file 
    # easy or hard
    ec.comp_decide(the_grid)
    print_board()

#testing the computer decision making
# comp_turn()
# comp_turn()
# for x in range(3): 
    # comp_turn()

# for x in range(3):
    # player_turn()

TIE_VALUE = -1 # TIE for the game, no more open spaces
IS_SPACE = 0 # there is more remaining spaces, do not yet result in tie
WINNER_1 = 1 # player 1 wins
WINNER_2 = 2 # player 2 wins
def determine_winner():
    # at end of each turn, look for any 3-in-a-row
    # any of the columns (3),
    # any of the rows (3), 
    # any of the diagonals (2)

    # return 0 if there are no winners
    # return 1 if player1 wins 
    # return 2 if player2 wins

    # return -1 if no players win, and the board is full , a tie

    col_result = check_the_columns()
    row_result = check_the_rows()
    diag_result = check_the_diagonals()
    # if col_result== TIE_VALUE or row_result == TIE_VALUE or diag_result == TIE_VALUE:
        # return TIE_VALUE
    
    # add the result values together


    # set the results in an array
    # and search for any values that match a condition for a player winning
    result_array = [ col_result, row_result, diag_result]
    if WINNER_1 in result_array:
        return WINNER_1
    elif WINNER_2 in result_array:
        return WINNER_2
    elif IS_SPACE in result_array:
        return IS_SPACE
    else: # with no winners, and no empty spaces, there is a tie
        return TIE_VALUE

def check_the_columns():
    # check the 3 colums for 3 of a kind, in a column
    # return 0 if no winner
    # return 1 if player1 wins
    # return 2 if player2 wins
    pass
    for x in range(3):
        first_cell = the_grid[0][x]
        for y in range(1,3):
            if first_cell != the_grid[y][x]:
                # if the second/third cell in a row does not match the first cell in a row
                # skip the row
                # continue
                break

            if y == 2 : 
                # reach the end of the row without a mismatch, then 3 in a row

                # check that the row is not empty
                if first_cell == h.empty_spot:
                    continue
                elif first_cell == h.player1:
                    return 1
                elif first_cell == h.player2:
                    return 2

    return 0



def check_the_rows():
    # check the row, 3 of a kind in a single row
    pass 
    for y in range(3): # cycle through the rows
        first_cell = the_grid[y][0]
        for x in range(1,3): # cycle through the columns within the row
            # if the not first cell does not match the first cell, skip this row
            # , and go to the next row
            if first_cell != the_grid[y][x]: 
                # continue
                break
            if x == 2 : 
                # reach the end of the row without a mismatch, then 3 in a row

                # check that the row is not empty
                if first_cell == h.empty_spot:
                    continue
                elif first_cell == h.player1:
                    return 1
                elif first_cell == h.player2:
                    return 2

    return 0


def check_the_diagonals():
    # check the diagonals
    result = 0
    # 0,0  1,1  2,2 (topleft to downright)
    # first_cell = the_grid[0][0]
    # for x in range(1,3):
    #     if first_cell != the_grid[x][x]: # the cells do not match 
    #         break
    # # 2,0 1,1 0,2 (topright to downleft)
    # first_cell = the_grid[0][2]
    # for y in range(1,3):
    #     if first_cell != the_grid[y][2-y]:
    #         break
    # return result

    # 0,0  1,1  2,2 (topleft to downright)
    diag1 = [ the_grid[0][0], the_grid[1][1], the_grid[2][2] ]
    # 2,0 1,1 0,2 (topright to downleft)
    diag2 = [ the_grid[2][0], the_grid[1][1], the_grid[0][2] ]

    if h.empty_spot in diag1 and h.empty_spot in diag2:
        # if both diagonals have an empty spot, there is no winner by diagonal
        # return ContinePlay
        return 0
    else:
        # there are no open spaces in the diagonals, return Tie, Player1, or Player2
        
        # if the diagonals are not all equal 
        # , there will only be one value in the set
        # diagonal1
        if len( set( diag1) ) == 1:
            # there is only one value
            if diag1[0] == h.player1:
                return 1
            elif diag[1] == h.player2:
                return 2
        # diagonal2
        if len( set(diag2) ) == 1:
            if diag2[0] == h.player1:
                return 1
            elif diag2[0] == h.player2:
                return 2

        

        else:
            # both diagaonals are filled, and neither have 1 value
            # return a Tie 
            return -1



def is_board_not_full():
    # boolean
    # return full if there are no more spaces available
    # if h.empty_spot in the_grid:
    if emp_spot  in the_grid:
        # there is an empty spot in the board 
        # return False
        return True
    else:
        # print("the board is full 1")
        # return True
        return False


def play_game():
    # loop through player/comp turns until winner or board full 

    current_state = 0
    # while current_state == 0:
    #     player_turn()
    #     comp_turn()
    #     current_state = determine_winner()
        
    # loop infinitely, breaking out when current_state == 0
    while True:
        player_turn()
        current_state = determine_winner() 
        if current_state != 0:
            break
        comp_turn() 
        current_state = determine_winner()
        if current_state != 0:
            break 

    print("Winner is ", current_state)

play_game()