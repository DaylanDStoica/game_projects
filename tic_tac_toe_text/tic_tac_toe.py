
# empty_spot = ''
# player1 = 'X'
# player2 = 'O'
# from header import empty_spot, player1, player2
import header as h

the_grid = [ ['']*3] * 3 # 3x3 grid 
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

def comp_turn():
    # use the decision algorithm from the chosen difficulty file 
    # easy or hard
    pass