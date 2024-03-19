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

#Write your code below this line 👇
import random
user_choice = int(input("Select 0 for Rock, 1 for Paper or 2 for Scissors: "))
pc = [0, 1, 2]
pc_choice = random.randint(0, len(pc) -1)

if user_choice == 0:
    print(f"{rock} Rock is your choice")
elif user_choice == 1:
    print(f"{paper} Paper is your choice")
elif user_choice == 2:
    print(f"{scissors} Scissors is your choice")

if pc_choice == 0:
    print(f"{rock} Rock is PC choice")
elif pc_choice == 1:
    print(f"{paper} Paper is PC choice")
elif pc_choice == 2:
    print(f"{scissors} Scissors is PC choice")