# score = int(input("Score:"))
# if score >= 5000:
#     print("New High Score!")
# else:
#     print("Keep trying")

# height = int(input("Height in inches:"))
# age = int(input("Age:"))
# if age >= 14 and height >= 65:
#     print("Welcome to the team")
# else:
#     print("Sorry, requirements not met")

# day = str(input("Day of the week:"))
# if day == "Saturday" or day == "Sunday":
#     print("Sleep in")
# else:
#     print("Time for school")

# age = int(input("What is your age:"))
# regular_price = 12
# free = 0
# adult_price = 15
# if age < 5 or age > 65:
#     print(f"Ticket Price: ${free}")
# elif 5 <= age <= 17:
#     print(f"Ticket Price: ${regular_price}")
# else:
#     print(f"Ticket Price: ${adult_price}")

# class_choice = str(input("Choose Class:"))
# strength = int(input("Choose your strength"))
# if class_choice == "warrior" and strength > 15:
#     print("Mighty Warrior")
# elif class_choice == "warrior" and strength <= 15:
#     print("Training Needed")
# else:
#     ("Different Path")

views = int(input("Enter View Count:"))
status = "viral" if views > 10000 else ("trending" if views > 1000 else "growing")
print(f"Video Status: {status}")