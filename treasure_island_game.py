# TASK
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

print("You are at a crossroad. Which way do you wan to continue: left or right? ")
way_to_go = input("Which way do you want to go? ").lower()
if way_to_go == "L".lower() or way_to_go == "left".lower():
  way_to_go = input("You are going to a lake. Would you like to 'wait' or you will catch a 'boat'? ")
  if way_to_go == "wait".lower():
    choices = input("Three doors showing in front of you, which one would you open: 'yellow', 'red' or 'blue'? ").lower()
    if choices == "blue":
      print("You are killed by falling in a deep pit. Game Over")
    elif choices == "red":
      print("Fire killed you. Game Over")
    elif choices == "yellow":
      print("You found an alarm clock that wakes you up in your bed. You WIN")
    else:
      print("Wrong choice. Game Over.")
  else:
    print("You are drawning, the boat is sinking")
else:
  print("You head was chopped. Game Over")