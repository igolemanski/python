from art import logo
print(logo)
print("Welcome to the secret auction program.")

bids = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? ")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)


# ANOTHER WAY TO SOLVE THE TASK
# print("Welcome to the secret auction program.")

# bidders = {}

# bidding_finished = False
# while not bidding_finished:
#   name = input("What is your name?: ")
#   bid = int(input("What's your bid?: $"))
#   bidders[name] = bid
#   more_bidders = input("Are there any other bidders? Type 'Yes' or 'No': ").lower()
#   if more_bidders == "no":
#     bidding_finished = True

# highest_bid = 0
# winner = ""

# for bidder, bid in bidders.items():
#   if bid > highest_bid:
#     highest_bid = bid
#     winner = bidder
# print(f"The winner is {winner} with a bid of ${highest_bid}.")