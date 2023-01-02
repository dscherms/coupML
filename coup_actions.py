#!/usr/bin/env python3
import sys
import random
from coup_callouts import *

def duke(Players,curr_deck,num_players,player_no,dead_list):

    # Check for callouts


    Players[player_no][2] += 3
    return Players

def ambassador(Players,curr_deck,num_players,player_no,dead_list):

     # Check for callouts



    # Reveal two cards from the deck 
    ambassador_deck = []
    ambassador_deck.append(Players[player_no][0])
    ambassador_deck.append(Players[player_no][1])
    card_one = curr_deck.pop(0)
    card_two = curr_deck.pop(0)
    ambassador_deck.append(card_one)
    ambassador_deck.append(card_two)

    # Choose two of the cards and replace other two in deck
    Players[player_no][0] = ambassador_deck.pop(random.choice(range(0,3))) # Add ML here
    Players[player_no][1] = ambassador_deck.pop(random.choice(range(0,2))) # Add ML here

    curr_deck.append(ambassador_deck.pop(0))
    curr_deck.append(ambassador_deck.pop(0))

    return Players, curr_deck

def captain(Players,curr_deck,num_players,player_no,dead_list):

     # Check for callouts

    
    # Create a list of available victims
    victim_list = []
    for i in range(4):
        if i != player_no and Players[i][3] and Players[i][2]:
            victim_list.append(i)

    # Choose which player to steal from
    victim = random.choice(victim_list) # add ML here

    # Check for callouts
    '''call_ambassador = random.choice(range(2)) # add ML here
    if call_ambassador:

        # Check for callouts


        return Players

    call_captain = random.choice(range(2)) # add ML here
    if call_captain:
        # Check for callouts


        return Players'''

    # Steal money from chosen player
    available_funds = Players[victim][2]
    if available_funds > 1:
        Players[victim][2] -= 2
        Players[player_no][2] += 2
    else:
        Players[victim][2] -= 1
        Players[player_no][2] += 1

    return Players

def assassin(Players,curr_deck,num_players,player_no,dead_list):

    # Create a list of available victims
    victim_list = []
    for i in range(4):
        if i != player_no and Players[i][3]:
            victim_list.append(i)

    # Choose which player to assassinate
    victim = random.choice(victim_list) # add ML here

    # Check for callouts
    if callout_function(Players,curr_deck,num_players,player_no,dead_list,'assassin'):
        return Players
    if claim_check(Players,curr_deck,num_players,player_no,dead_list,'contessa',victim):
        return Players

    # Assassinate victim
    if Players[victim][3] == 2:
        card_choice = random.choice(range(2)) # Add ML here
        dead_card = Players[victim][card_choice] 
        dead_list.append(dead_card)
        Players[victim][card_choice] = None
        Players[victim][3] -= 1
    elif Players[victim][3] == 1:
        if Players[victim][0]:
            dead_card = Players[victim][0]
            Players[victim][0] = None
        else:
            dead_card = Players[victim][1]
            Players[victim][1] = None
        dead_list.append(dead_card)
        Players[victim][3] -= 1

    return Players,dead_list

def foreign_aid(Players,curr_deck,num_players,player_no,dead_list):

    # Check for callouts
    if claim_check(Players,curr_deck,num_players,player_no,dead_list,'foreign_aid',None):
        return Players

    Players[player_no][2] += 2
    return Players

def income(Players,curr_deck,num_players,player_no):

    Players[player_no][2] += 1
    return Players

def coup(Players,curr_deck,num_players,player_no,dead_list):
    # Create a list of available victims
    victim_list = []
    for i in range(4):
        if i != player_no and Players[i][3]:
            victim_list.append(i)

    # Choose which player to assassinate
    victim = random.choice(victim_list) # add ML here

    if Players[victim][3] == 2:
        card_choice = random.choice(range(2)) # Add ML here
        dead_card = Players[victim][card_choice] 
        dead_list.append(dead_card)
        Players[victim][card_choice] = None
        Players[victim][3] -= 1
    elif Players[victim][3] == 1:
        if Players[victim][0]:
            dead_card = Players[victim][0]
            Players[victim][0] = None
        else:
            dead_card = Players[victim][1]
            Players[victim][1] = None
        dead_list.append(dead_card)
        Players[victim][3] -= 1

    # Cost of 7 dollars
    Players[player_no][2] -= 7

    return Players,dead_list





