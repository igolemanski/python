# ROCK PAPER SCISSORS Game

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
player = int(input("Select your number: "))
pc = [0, 1, 2]
random_num = random.randint(0, len(pc) - 1)

if player == 0 and random_num == 2:
    print(f"{rock} Rock WIN")
    print(f"{scissors} Scissors lose")
elif player == 2 and random_num == 1:
    print(f"{scissors} Scissors WIN")
    print(f"{paper} Paper lose")
elif player == 1 and random_num == 0:
    print(f"{paper} Paper WIN")
    print(f"{rock} Rock Lose")
else:
    print("REMY")