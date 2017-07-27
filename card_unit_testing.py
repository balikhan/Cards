from Card import Card, Deck, Hand
#from Hand import Hand

#verbose = True

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
    main_deck.sort()
    main_deck.add_card(popped_card)
    #print(main_deck)
    print("Deck testing successful")


def deal_hand(deck):
    """ Veneer function for dealing hands """
    return deck.deal_hands(4,13)

def print_hands(hand_list):
    """ Pretty prints all the cards in each hand """
    if hand_list == None or len(hand_list) == 0:
        print("No hands in list")
    else:
        for hand in hand_list:
            print(hand.label + "\n" + str(hand) + "\n")

main_deck = Deck()
main_deck.shuffle()            
hands = deal_hand(main_deck)
print_hands(hands)

#check_comparisons()
#check_deck()

