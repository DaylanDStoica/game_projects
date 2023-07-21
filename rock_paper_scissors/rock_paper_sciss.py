
# !/bin/usr/python3

# the driver of the game

potential_choices = ["rock", "paper", "scissor"]
def get_player_choice():
    player_choice = input("choose one of the choices")
    player_char = player_choice[0] # get the first char of the player's choice 
    # r=rock, p=paper, s=scissor
    player_raw = input("choose (R/P/S): ")
    player_choice = player_raw[0].lower() # get the lower case of the first index 
    return player_choice

import random
def generate_comp_choice():
    comp_choice = random.choice(potential_choices)
    return comp_choice 

    