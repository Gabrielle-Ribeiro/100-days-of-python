from art import logo

still_bidders = True
bidders = {}

while still_bidders:
    print(logo)
    name = input("What's your name?: ")
    bid = int(input("What's your bid?: $"))

    bidders[name] = bid

    answer = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if answer == 'no':
        still_bidders = False

bigger_bid = 0
winner = ""

for bidder, bid in bidders.items():
    if bid > bigger_bid:
        bigger_bid = bid 
        winner = bidder

print(f"The winner is {winner} with a bid of ${bigger_bid}.")