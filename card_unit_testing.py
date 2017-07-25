from Card import *

def check_comparisons():
    card1 = Card(1, 5)
    card2 = Card(2, 5)
    card3 = Card(1, 4)
    card4 = Card(2, 5)
    
    assert card1 > card3
    assert card1 < card2
    assert card2 == card4
    assert card3 != card2
    print("Tests successful")
    
    
check_comparisons()