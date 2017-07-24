class Card(object):
    """
    Card class - has attributes rank and suit
    """
    
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    
    def __init__(self, suit=0, rank=2):
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        return "%s of %s" % (Card.rank_names[self.rank], Card.suit_names[self.suit])
        
        
c1 = Card(2,6)
print(c1)