from random import randrange

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def get_random_cards():
    '''
    Get a new random card from deck.
    '''
    r = randrange(0,12,1)
    return cards[r]

# def add_new_cards_hand(qty):
#     '''
#     Add card qnt to hand.
#     '''
#     for n in range(0, qty):
#         return get_random_cards()

# hand = []
# hand.append(add_new_cards_hand(2))
# print(hand)