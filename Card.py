import random

class Card():
    """
    Card class - has attributes rank and suit
    """
    
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    
    def __init__(self, suit=0, rank=2):
        self.rank = rank
        self.suit = suit
        
    def __lt__(self, other):
        return self.suit < other.suit or (self.suit == other.suit and self.rank < other.rank)
        
    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank
    
    def __str__(self):
        return "%s of %s" % (Card.rank_names[self.rank], Card.suit_names[self.suit])
        

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
        """ constructs a string from the self.deck list """
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)
    
    def pop_card(self, i=-1):
        """ Removes the last card from the list and returns it 
        Uses variable i for position of poppage. Pops last card
        by default """
        return self.cards.pop(i)
        
    def add_card(self, card):
        """ Adds a given card to the deck, but returns nothing """
        self.cards.append(card)
        
    def remove_card(self, card):
        """ Removes a given card from the deck, returns nothing """
        self.cards.remove(card)
        
    def shuffle(self):
        """ shuffles cards, returns nothing """
        random.shuffle(self.cards)
        
    def sort(self):
        """ sorts cards, returns nothing """
        self.cards.sort()
        
    def move_cards(self, hand, num):
        """ moves num cards from deck list to
        hand list. will also work in reverse
        with hand to deck transfer """
        
        # Check to see if the deck has enough cards
        if len(self.cards) < num:
            print("There aren't enough cards in the stack")
            return
        
        for i in range(num):
            hand.cards.append(self.cards.pop())
            
    def deal_hands(self, num_hands, num_cards):
        # check to see if there are enough cards to deal
        if len(self.cards) < num_hands*num_cards:
            print("There aren't enough cards in the stack")
            return
        
        res = []
        for hand in range(num_hands):
            label = "Hand " + str(hand)
            hand = Hand(label)
            self.move_cards(hand, num_cards)
            res.append(hand)
        return res
            
class Hand(Deck):
    """
    Hand class - child of Deck class 
    Attributes - cards, label
    """
    
    def __init__(self, label=""):
        self.cards = []
        self.label = label