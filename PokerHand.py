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
    
    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise. """
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 2:
                return True
        return False
    
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
        self.rank_hist()
        for val in self.ranks.values():
            if val >= 3:
                return True
        return False
    
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
        prev_rank = rank_list[0]
        straight_count = 0
        for rank in rank_list[1:]:
            if rank - prev_rank == 1:
                straight_count += 1
            else:
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
        pass
    
    def has_four_kind(self):
        """Returns True if the hand has a four of a kind, False otherwise. """
        pass
    
    def has_straight_flush(self):
        """Returns True if the hand has a straight flush, False otherwise. """
        pass


if __name__ == '__main__':
    # make a deck
    deck = Deck()
    deck.shuffle()

    # deal the cards and classify the hands
    for i in range(7):
        hand = PokerHand()
        deck.move_cards(hand, 7)
        hand.sort()
        print (hand)
        print (hand.has_straight())
        print ('')
        

