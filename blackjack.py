# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 20:45:35 2020

@author: Dylan
"""
import random
import time

deck = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
player_hand = []
dealer_hand = []
import random
card = random.choice(cards)
player_hand.append(card)
def card_value(card):
 if card == 'A':
 return 11
 elif card == 'K' or card == 'Q' or card == 'J':
 return 10
 else:
 return int(card)
def hand_total(hand):
 total = 0
 for card in hand:
 total += card_value(card)
 return tota