
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
    pass
    # print(" please give 2 integers for your spot (1-3), (row, col):  ", end='')
    # input1 = input().split()
    # y = int(input1[0])
    # x = int(input1[1])

    print(" please give 2 integers for your spot (1-3), (x, y):  ", end='')
    input1 = input().split()
    x = input1[0]
    y = input[1]

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

def determine_winner():
    # at end of each turn, look for any 3-in-a-row
    # any of the columns (3),
    # any of the rows (3), 
    # any of the diagonals (2)

    # return 0 if there are no winners
    # return 1 if player1 wins 
    # return 2 if player2 wins

    # return -1 if no players win, and the board is full , a tie

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

def check_the_diagonals():
    # check the diagonals
    # 0,0  1,1  2,2 (topleft to downright)
    # 2,0 1,1 0,2 (topright to downleft)
    pass


