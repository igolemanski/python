# TASK - write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
import random

num = random.randint(0, 1)

if num == 0:
  print("Heads")
else:
  print("Tails")

import random
names = ["Ivo", "Niki", "Jivko", "Gosho", "Ico"]
random_num = random.randint(0, len(names) -1)
random_names = names[random_num]
print(f"{random_names} is going to pay the bill")