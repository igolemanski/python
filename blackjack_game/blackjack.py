import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(random_card):
    return random.choice(random_card)

user_cards = []
user_cards.append(deal_card(cards))
user_cards.append(deal_card(cards))
print(user_cards)

computer_cards = []
computer_cards.append(deal_card(cards))
computer_cards.append(deal_card(cards))
print(computer_cards)


def calculate_score(user_cards):
    blackjack = user_cards[0] + user_cards[1]
    if blackjack == 21:
        return 0
    else:
        return sum(user_cards)

def calculate_score(computer_cards):
    blackjack = computer_cards[0] + computer_cards[1]
    if blackjack == 21:
        return 0
    else:
        return sum(computer_cards)

test = calculate_score(computer_cards)
print(test)