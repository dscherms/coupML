#!/usr/bin/env python3
import sys
import random


def setup_players(num_players):

    Players = []
    dead_list = []
    curr_deck = ['ambassador','ambassador','ambassador','contessa','contessa','contessa','captain','captain','captain','duke','duke','duke','assassin','assassin','assassin']
    random.shuffle(curr_deck)

    for i in range(num_players):
        card_one = curr_deck.pop(0)
        card_two = curr_deck.pop(0)

        # Players setup: [CARD ONE,CARD TWO,MONEY,REMAINING CARDS]
        Players.append([card_one,card_two,2,2])

    return Players, curr_deck, dead_list
