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
    return total


def deal_cards():
    player_hand.append(random.choice(deck))
    player_hand.append(random.choice(deck))
    dealer_hand.append(random.choice(deck))
    dealer_hand.append(random.choice(deck))


def deal_hit(turn):
    if turn == 1:
        player_hand.append(random.choice(deck))
    else:
        dealer_hand.append(random.choice(deck))


def display_hand(hand):
    display = ""
    for card in hand:
        if len(display) > 0:
            display += ","
        display += card
    return display


print("")
print("")
print("")
print("--------------------WELCOME TO BLACKJACK---------------------")
print("")
time.sleep(1)
print("")

play_again = "Yes"

while play_again == "Yes" or play_again == "yes":

    deal_cards()
    turn = 1
    player_bust = False
    display = display_hand(player_hand)
    print("Your hand: %s" % display)

    while turn == 1:
        print("Do you want a hit?")
        hit = input("Yes or No: ")
        if hit == "Yes" or hit == "yes":
            deal_hit(turn)
            display = display_hand(player_hand)
            print("Your hand: %s" % display)
            player_points = hand_total(player_hand)
            if (player_points > 21):
                print("You Bust!")
                player_bust = True
                turn = 2
        else:
            turn = 2

    dealer_bust = False
    dealer_points = hand_total(dealer_hand)
    display = display_hand(dealer_hand)
    print("Dealer's hand: %s" % display)

    time.sleep(1)

    if player_bust:
        print("Dealer Wins!")
    else:
        if dealer_points < 16:
            deal_hit(turn)
            print("Dealer hit...")
            time.sleep(1)
            display = display_hand(dealer_hand)
            print("Dealer's hand: %s" % display)
            dealer_points = hand_total(dealer_hand)
            if dealer_points > 21:
                time.sleep(1)
                print("Dealer Busts!")
                dealer_bust = True

            time.sleep(2)

        player_points = hand_total(player_hand)
        dealer_points = hand_total(dealer_hand)

        if player_points > dealer_points or dealer_bust:
            print("You Win with %s!!!" % player_points)
        else:
            print("Dealer Wins with %s!!!" % dealer_points)

    time.sleep(2)

    print("")
    print("Do you want to play again?")

    player_hand.clear()
    dealer_hand.clear()

    play_again = input("Yes or No: ")
    print("")










