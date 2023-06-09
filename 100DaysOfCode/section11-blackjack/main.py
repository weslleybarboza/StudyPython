############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import cards as c

# input("Do you want to play a game of Blackjack? Type 'y'or 'n': ").lower
print(logo)

hand_players = {
    "player" : [],
    "computer" : []
}

#start the game with score < 21

# def add_cards_player(player, qty):

# while init_grant_than_21:
#     c.add_new_cards_hand(hand, qty)
#     score = sum(hand)
#     if score < 21:
#         init_grant_than_21 = False
#     return hand

qty = 2
for player in hand_players:
    score = 0
    while score < 21:
        for card in range(0, qty):
            hand_players[player].append(c.get_random_cards())
            score = sum(hand_players[player])

print(hand_players)

# print(f"    Your cards: {card_hand}, current score: {score}.")