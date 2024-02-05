# TASK
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))

    if age < 12:
        bill = 5
        print("Your bill is", bill, "dollars")
    elif age >= 12 and age <= 18:
        bill = 7
        print("Your bill is", bill, "dollars")
    elif age > 18 and age < 45:
        bill = 12
        print("Your bill is", bill, "dollars")
    elif age >= 45 and age <= 55:
        print("You can enter for free")

    want_photos = input("Would you like a photo? ")
    if want_photos == "y":
        bill += 3
        print("Your bill is", bill, "dollars")
    else:
        print("No photo added")
else:
    print("You can not ride the rollercoaster")