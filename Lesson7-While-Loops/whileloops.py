# count = 5            # 1 Initialize

# while count > 0:     # 2 Check Condition
#     print(count)
#     count -= 1       # 3 Update
# print("Blast Off")

# # Part 1 Quick Practice 

# count = 1

# while count < 11:
#     print(count)
#     count += 1


# text = "Bergen Tech"

# i = 0
# while i < len(text):
#     print(text[i])
#     i += 1

# result = ""
# while i < len(text):
#     char = text[i]
#     if 'A' <= char <= 'Z':
#         result += char 
#     i += 1
# print(result)

# Age Validator
# age = -1
# while age < 0 or age > 120:
#     age = int(input("Enter Your Age: "))
#     if age < 0 or age > 120:
#         print("Invalid!")
# print(f"Your age is {age}")

# Break

# while True:
#     answer = input("Continue? ")
#     if answer == "no":
#         break
#     print("Going ... ")

# print("Done!")

# Continue Statement

# count = 0 
# while count < 5:
#     count += 1
#     if count == 3:
#         continue # skips over 3
#     print(count)

# number = 7 
# while True:
#     guess = int(input("Pick a number: "))
#     if guess < 7:
#         print("Higher")
#         continue
#     elif guess > 7:
#         print("Lower")
#         continue
#     else:
#         print("Correct")
#         break

total = 0
while True:
    number = int(input("Pick a number "))
    if number < 0 or number > 0:
        total += number
    else:
        print(f"Total: {total}")
        break
# Alternative
# total = 0
# number = int(input("Enter a number: "))

# while number != 0:
#     total += number
#     number = int(input("Enter a number: "))

# print(f"Sum: {total}")