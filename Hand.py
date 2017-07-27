from Deck import *
from Card import *

class Hand(Deck):
    """
    Hand class - child of Deck class 
    Attributes - cards, label
    """
    
    def __init__(self, label=""):
        self.cards = []
        self.label = label
        
    