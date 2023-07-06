

the_grid = [ ['']*3] * 3 # 3x3 grid 
def print_board():
    for y in range(len(the_grid)):
        for x in range(len(the_grid[y])):
            print('|', the_grid[y][x], end = ' ')
        print()
        print( '-'*10)
        

print_board()