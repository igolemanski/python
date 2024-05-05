import random
from game_data import data
from art import logo, vs

def account_info(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """Take the users guess and follower counts and return if they got it right."""
    if a_account_followers > b_account_followers:
        return guess == "a"
    else:
        return guess == "b"

# Display art.
print(logo)
score = 0

# Make the game repeatable.
game_should_continue = True

# Generate a random account from the game data.
b_account = random.choice(data)

while game_should_continue:

    # Making account at positiona B become the next account at position A.

    a_account = b_account
    b_account = random.choice(data)
    while a_account == b_account:
        b_account = random.choice(data)


    print(f"Compare A: {account_info(a_account)}")
    print(vs)
    print(f"Against B: {account_info(b_account)}")

    # Ask user for a guess.
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is correct.
    # Ger follower count of each account.
    a_account_followers = a_account["follower_count"]
    b_account_followers = b_account["follower_count"]

    is_correct = check_answer(guess, a_account_followers, b_account_followers)

    # Give user feedback on their guess.
    if is_correct:
        score += 1
        print(f"You are right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry you are wrong. Final score: {score}.")


