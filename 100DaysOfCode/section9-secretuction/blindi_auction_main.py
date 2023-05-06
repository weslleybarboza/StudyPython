from replit import clear
from blind_auction_art import logo

print(logo)

bids_list = {}
news_bids = True

while news_bids:
    name = input("Insert the name: \n")
    bid_price = float(input("Insert the bid: \n"))
    bids_list[name] = bid_price
    response = input("Is there other bid? (Y or N) \n").lower()
    if response == "n":
        news_bids = False
    clear()

winner = max(bids_list, key=bids_list.get)

print(f"The winner is: {winner} and the bid was {bids_list[winner]}.")

