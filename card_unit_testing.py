from Deck import Deck
#from Hand import Hand

def check_comparisons():
    card1 = Card(1, 5)
    card2 = Card(2, 5)
    card3 = Card(1, 4)
    card4 = Card(2, 5)
    
    assert card1 > card3
    assert card1 < card2
    assert card2 == card4
    assert card3 != card2
    print("Card testing successful")
    
def check_deck():
    main_deck = Deck()
    
    assert len(main_deck.cards) == 52
    print("Shuffling main deck")
    main_deck.shuffle()
    #print(main_deck)
    popped_card = main_deck.pop_card()
    print(popped_card)
    print("Sorting main deck")
    main_deck.sort_deck()
    main_deck.add_card(popped_card)
    #print(main_deck)
    print("Deck testing successful")


def deal_hand(deck):
    return deck.deal_hands(4,7)

hands = deal_hand(Deck())
for hand in hands:
    
    print(hand.label, hand.cards)
#check_comparisons()
#check_deck()

