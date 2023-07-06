
# Daylan Stoica

# @DaylanDStoica


# build the dice object and functions
# allow a variable in potential dice-rolls, with varying dice

# percentile rolls two dice, d100 (10-sided, 00-90), and d10 (1-10)

import random
class Die:
    def __init__ (self, num_of_sides = 6, lowest_val = 1):
        self.num_of_sides = num_of_sides
        self.lowest_val = lowest_val
        
    def roll_the_die(self):
        # randomly roll the die
        # return a random side value
        return random.randint( self.lowest_val, self.num_of_sides)
    


def test_all_dice_rolls ( ):
    types_of_dice = [3, 6, 10, 20, 100] # d3, d6, d10, d20, and percentile
    dice_list = []

    for x in types_of_dice:
        dice_list.append( Die(x) )
        print("d" , dice_list[-1].num_of_sides , " rolls a value of " , dice_list[-1].roll_the_die() )
    # print(dice_list.num_of_sides)
    
    
for x in range(100):
    test_all_dice_rolls()