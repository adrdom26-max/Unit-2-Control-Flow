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
age = -1
while age < 0 or age > 120:
    age = int(input("Enter Your Age: "))
    if age < 0 or age > 120:
        print("Invalid!")
print(f"Your age is {age}")