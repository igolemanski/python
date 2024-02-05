# EXAMPLE. The user is selecting the position and the that position is marked with "X"
line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

if position == "A1":
  line1[0] = "X"
elif position == "A2":
  line2[0] = "X"
elif position == "A3":
  line3[0] = "X"

if position == "B1":
  line1[1] = "X"
elif position == "B2":
  line2[1] = "X"
elif position == "B3":
  line3[1] = "X"

if position == "C1":
  line1[2] = "X"
elif position == "C2":
  line2[2] = "X"
elif position == "C3":
  line3[2] = "X"

print(f"{line1}\n{line2}\n{line3}")
