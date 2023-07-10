
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
    print(" please give 2 integers for your spot (1-3), (row, col):  ", end='')
    input1 = input().split()
    y = int(input1[0])
    x = int(input1[1])
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