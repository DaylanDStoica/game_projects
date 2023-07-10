
# empty_spot = ''
# player1 = 'X'
# player2 = 'O'
# from header import empty_spot, player1, player2
import my_header as h

the_grid = [ [h.empty_spot]*3] * 3 # 3x3 grid 
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

import easy_comp as ec 
def comp_turn():
    # use the decision algorithm from the chosen difficulty file 
    # easy or hard
    ec.comp_decide(the_grid)
    print_board()

# comp_turn()
# comp_turn()
for x in range(3): 
    comp_turn()