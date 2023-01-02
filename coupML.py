#!/usr/bin/env python3
import sys
import random
from setupML import *
from coup_actions import *

num_players = 4

# Main Execution

def main():
    Players, curr_deck, dead_list = setup_players(num_players)
    
    print(Players)
    print(curr_deck)

    Players = foreign_aid(Players,curr_deck,num_players,2,dead_list)
    print(Players)
    print(dead_list)



if __name__ == '__main__':
    main()