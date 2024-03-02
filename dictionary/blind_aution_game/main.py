# from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("Welcome to the secret auction program.")
name = input("What is your name?: ")
bid = int(input("What is your bid?: $"))

final_auction = {
    "name": "bid"
}
def auction(bidder, money):
    auction[bidder] = name
    auction[money] = bid
    final_auction.append(auction)

    other_buyers = input("Is there any other buyers?: ")
    if other_buyers == "yes":
        person  