# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 18:16:49 2017

@author: Khochi
"""
from Card import *
from Hand import *
import random

class Deck(object):
    """ 
    Deck class - holds a list of card objects
    """
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                self.cards.append(Card(suit, rank))
    
    def __str__(self):
        # constructs a string from the self.deck list
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)
    
    def pop_card(self):
        # removes the last card from the list and
        # returns it
        return self.cards.pop()
        
    def add_card(self, card):
        # adds a given card to the deck, but returns
        # nothing.
        self.cards.append(card)
        
    def shuffle(self):
        # shuffles cards, returns nothing
        random.shuffle(self.cards)
        
    def sort_deck(self):
        # sorts cards, returns nothing
        self.cards.sort()
        
    def move_card(self, hand, num):
        # moves num cards from deck list to
        # hand list. will also work in reverse
        # with hand to deck transfer
        #
        # Probably need to add some safety
        # code in case there are no more
        # cards left in the deck
        for i in range(num):
            hand.cards.append(self.cards.pop())
            
    def deal_hands(self, num_hands, num_cards):
        res = []
        for hand in range(num_hands):
            hand = Hand()
            self.move_card(hand, num_cards)
            res.append(hand)