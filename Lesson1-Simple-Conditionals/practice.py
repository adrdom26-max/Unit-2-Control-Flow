height_in_inches = int(input("Your Height in Inches:"))
if height_in_inches >= 72:
    print("You are tall!")
if height_in_inches <= 60:
    print("You are short.")
if height_in_inches > 60 and height_in_inches < 72: 
    print("You are Average.")

#SECOND WAY
height = int(input("Enter your height in inhes:"))

if height >= 72:
    print("You are tall!")
else:
    if height >= 60:
        print("You are average height!")
    else:
        print("You are short")