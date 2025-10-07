# # Lesson 5: For Loops 

# # PART 1: QUICK PRACTICE - Username Loop
# # =====================================
# # Write a for loop to print each character in this username

# username = "gamer2024"

# username[0]
# username[1]
# username[-1]
# username[len(username)-1]
# # Your for loop here
# for letter in username:
#     print(letter)

# range(5) # 0-5
# range(5,50,5) #5-50 (5,10,15,20,...,45)
# range(10,2,-2) # (10,8,6,4)

# for i in range(len(username)):
#     print(username[i])
# # PART 2: CODE ALONG - Username Validator
# # =====================================
# # Build a username validator that checks:
# # - Has at least one number
# # - Has at least one uppercase letter
# # - Count total characters

# username = "CoolGamer123"
# char = ''
# # upper case check
# 'A' <= char <= 'Z'
# # lower case check
# 'a' <= char <= 'z'
# # Your code here
# username = input("Enter your username:")
# has_number = False
# has_uppercase = False
# total_chars = len(username)

# for char in username:
#     if 'A' <= char <= 'Z':
#         has_uppercase = True
#     if '0' <= char <= '9':
#         has_number = True

# print(f"Username: {username}")
# print(f"Total Characters: {total_chars}")
# print(f"Has Number: {has_number}")
# print(f"Has Uppercase: {has_uppercase}")
# PART 3: QUICK PRACTICE - Counting 'e'
# =====================================
# Count how many times the letter 'e' appears (case-insensitive)

# tweet = "Hello everyone! Hope you're having a great day!"

# e_count = 0
# # Your loop here
# for char in tweet:
#     if char == 'e': 
#         e_count += 1

# print(f"E count: {e_count}")

# PART 4: CODE ALONG - Message Repeater
# =====================================
# Build a message repeater with countdown:
# - Print a message multiple times
# - Add a countdown before each message
# Example: "3... Study hard!"

# message = "Study hard!"
# times = 5

# # Your code here
# print('\n ---Message Repeater---')
# for i in range(times, 0, -1):
#     print(f"{i}... {message}")

# PART 5: YOUR TURN - Text Message Analyzer
# ========================================
# - Total characters (use len())
# - Number of spaces
# - Number of letters
# - Number of punctuation marks (! ? . ,)

# text = "Hey! How are you doing today? :)"

# # Your analysis code here
# punctuation = 0
# total_char = len(text)
# spaces = 0
# letters = 0
# for char in text:
#     if char == ' ':
#         spaces += 1
#     if 'a' <= char <= 'z' or ('A' <= char <= 'Z'):
#         letters += 1
#     if (char == '!') or (char == '?') or (char == ',') or (char == '.'):
#         punctuation += 1


# print(f"Total Characters: {total_char}")
# print(f"Letters: {letters}")
# print(f"Spaces: {spaces}")
# print(f"Punctuation: {punctuation}")
# # PART 6: PATTERN CHALLENGE

# # ============================================================================

# # Challenge A: Print squares of numbers 1-5 (1, 4, 9, 16, 25)
# for i in range(1, 6):
#     print(i ** 2)

# Challenge B: Print countdown from 10 to 1
for i in range(10, 0, -1):
    print(i)

# Challenge C: Print every 3rd number from 0 to 15 (0, 3, 6, 9, 12, 15)
for i in range(0, 16, 3):
    print(i)
