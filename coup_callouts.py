#!/usr/bin/env python3
import sys
import random

def claim_check(Players,curr_deck,num_players,player_no,dead_list,type,victim):
    
    is_claimed = random.choice(range(2))
    # Create a list of available victims
    claimer_list = []
    for i in range(4):
        if i != player_no and Players[i][3] and Players[i][2]:
            claimer_list.append(i)

    # Choose which player to steal from
    claimer = random.choice(claimer_list) # add ML here

    if is_claimed:
        if type == 'foreign_aid':
            # Add callout 
            if callout_function(Players,curr_deck,num_players,claimer,dead_list,'duke'):
                return False
            return True
        else:
            if callout_function(Players,curr_deck,num_players,claimer,dead_list,type):
                return False
            return True
    
    return False

def callout_function(Players,curr_deck,num_players,player_no,dead_list,type):

    is_calledout = random.choice(range(2))

    claimer_list = []
    for i in range(4):
        if i != player_no and Players[i][3] and Players[i][2]:
            claimer_list.append(i)
    
    claimer = random.choice(claimer_list) # add ML here

    if is_calledout:
        if Players[player_no][0] == type or Players[player_no][0] == type:
            if Players[claimer][3] == 2:
                card_choice = random.choice(range(2)) # Add ML here
                dead_card = Players[claimer][card_choice] 
                dead_list.append(dead_card)
                Players[claimer][card_choice] = None
                Players[claimer][3] -= 1
            elif Players[claimer][3] == 1:
                if Players[claimer][0]:
                    dead_card = Players[claimer][0]
                    Players[claimer][0] = None
                else:
                    dead_card = Players[claimer][1]
                    Players[claimer][1] = None
                dead_list.append(dead_card)
                Players[claimer][3] -= 1
        else:
            if Players[player_no][3] == 2:
                card_choice = random.choice(range(2)) # Add ML here
                dead_card = Players[player_no][card_choice] 
                dead_list.append(dead_card)
                Players[player_no][card_choice] = None
                Players[player_no][3] -= 1
            elif Players[player_no][3] == 1:
                if Players[player_no][0]:
                    dead_card = Players[player_no][0]
                    Players[player_no][0] = None
                else:
                    dead_card = Players[player_no][1]
                    Players[player_no][1] = None
                dead_list.append(dead_card)
                Players[player_no][3] -= 1
                return True

    return False


        