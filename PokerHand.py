"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *


class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
    
    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
            
    def suit_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
    
    def check_same_rank(self, num_cards):
        """ Returns if the hand has num_cards of the same rank, False otherwise"""
        self.rank_hist()
        for val in self.ranks.values():
            if val >= num_cards:
                return True
        return False
        
    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise. """
        return self.check_same_rank(2)
    
    def has_two_pair(self):
        """Returns True if the hand has a two pair, False otherwise. """
        self.rank_hist()
        pair_counter = 0
        for val in self.ranks.values():
            if val >= 2:
                pair_counter += 1
                if pair_counter >= 2:
                    return True
        return False
    
    def has_three_kind(self):
        """Returns True if the hand has a three of a kind, False otherwise. """
        return self.check_same_rank(3)
    
    def has_straight(self):
        """ Returns True if the hand has a straight, False otherwise """
        self.rank_hist()
        rank_list = list(self.ranks.keys())
        rank_list.sort()
        # rank_list has to have five unique ranks to make a straight
        if len(rank_list) < 5: return False
        # if 1 (Ace) exists, then we want to add 14 to make sure top
        # end straight (Q,K,A) is counted
        if 1 in rank_list: rank_list.append(14)
        # Walk through list and make sure ranks are sequential
        # If 4 counted in a row (1 is without counting any), then return True 
        prev_rank = rank_list[0]
        straight_count = 0
        for rank in rank_list[1:]:
            if rank - prev_rank == 1:
                straight_count += 1
            else:
                # Reset straight count if chain broken, start from new card
                straight_count = 0
            if straight_count >= 4:
                return True
            prev_rank = rank
        return False
            
    
    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise. """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
    
    def has_full_house(self):
        """Returns True if the hand has a full house, False otherwise. """
        self.rank_hist()
        rank_vals = list(self.ranks.values())
        rank_vals.sort(reverse=True)
        if sum(rank_vals[:2]) >= 5:
            return True
        else:
            return False
    
    def has_four_kind(self):
        """Returns True if the hand has a four of a kind, False otherwise. """
        return self.check_same_rank(4)
    
    def has_straight_flush(self):
        """Returns True if the hand has a straight flush, False otherwise. """
        
        self.suit_hist()
        # create a zipped list to be reverse sorted to get the
        # max frequency and associated suit number
        suit_rank = list(zip(self.suits.values(),self.suits.keys()))
        suit_rank.sort(reverse=True)
        # if max suit freq is not greater than 5, then no flush
        if not suit_rank[0][0] >= 5: return False
        
        suit_hand = PokerHand()
        max_suit = suit_rank[0][1]
        
        # Create a sub hand with only cards of the max suit
        # and then run the has_straight function on it
        for card in self.cards:
            if card.suit == max_suit:
                suit_hand.add_card(card)
        return suit_hand.has_straight()
    
    def classify(self):
        """ Classifies the current hand according to cards """
        if self.has_straight_flush():
            self.label = "Straight Flush"
        elif self.has_four_kind():
            self.label = "Four of a Kind"
        elif self.has_full_house():
            self.label = "Full House"
        elif self.has_flush():
            self.label = "Flush"
        elif self.has_straight():
            self.label = "Straight"
        elif self.has_three_kind():
            self.label = "Three of a Kind"
        elif self.has_two_pair():
            self.label = "Two Pair"
        elif self.has_pair():
            self.label = "Pair"
        else:
            self.label = "Nothing"

def check_deck():
    deck = Deck()
    deck.shuffle()
    num_hands = 7
    # deal the cards and classify the hands
    for i in range(num_hands):
        hand = PokerHand()
        deck.move_cards(hand, 52//num_hands)
        hand.sort()
        print (hand)
        hand.classify()
        print (hand.label)
        print ('')

def check_hand():
    hand = PokerHand()
    hand.add_card(Card(1,1))
    hand.add_card(Card(1,10))
    hand.add_card(Card(1,11))
    hand.add_card(Card(1,12))
    hand.add_card(Card(2,6))
    hand.add_card(Card(1,13))
    return hand.has_straight_flush()
    
if __name__ == '__main__':
    # make a deck
    print(check_deck())
        

