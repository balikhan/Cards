from Card import *

def check_lt():
    card1 = Card(1, 5)
    card2 = Card(2, 5)
    card3 = Card(1, 4)
    
    print("Card 1 < Card 2 (True):", card1 < card2)
    print("Card 3 < Card 1 (True):", card3 < card1)
    print("Card 3 < Card 2 (True):", card3 < card2)
    print("Card 2 < Card 1 (False):", card2 < card1)
    print("Card 1 < Card 3 (False):", card1 < card3)
    print("Card 2 < Card 3 (False):", card2 < card3)
    
check_lt()