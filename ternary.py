# Lesson 4: Ternary Operator & Chained Comparisons

# =============================================================================
# PART 1: TERNARY OPERATOR BASICS
# =============================================================================

# Traditional if-else way
age = 17
if age >= 18:
    status = "adult"
else:
    status = "minor"

print(f"Traditional way: {status}")
# Ternary operator way (one line)
# Pattern: variable = value1 if condition else value2
status = "adult" if age >= 18 else "minor"
print(f"Ternary Way: {status}")

# =============================================================================
# PART 2: MORE TERNARY EXAMPLES
# =============================================================================

# Weather clothing choice
temperature = 75
# Use ternary to choose between "shorts" and "jacket"
clothing = "shorts" if temperature is > 70 else "jacket" 
print(f"Outfit: {clothing}")

# Grade pass/fail status  
score = 85
# Use ternary to set passed to "yes" or "no"
passed = "yes" if score >= 70 else "no"
print(f"Score: {score}, Passed: {passed}")
# =============================================================================
# PART 3: CHAINED COMPARISONS
# =============================================================================

# Traditional way with 'and'
age = 16
# Write if statement: age >= 13 and age <= 19
if age >= 13 and age <= 19:
    print(f"Traditional: You are a teenager")

# Chained comparison way (like math)
# Pattern: if min_value <= variable <= max_value
if 13 <= age >= 19:
    print("Chained: You are a teenager")

# Grade range checking
grade = 87
# Use chaining to check if grade is B range (80-89)
if 80 <= grade < 89:


# =============================================================================
# PART 4: PRACTICE CONVERSIONS
# =============================================================================

# Convert these to ternary:

# 1. Tired drink choice

# if tired:
#     drink = "coffee"
# else:
#     drink = "water"


# 2. Student pricing
is_student = False
# if is_student:
#     price = 10
# else:
#     price = 15

price = 10 if is_student else 15
print(f"Ticket Price: ${price}")
# Convert these to chained comparisons:

# 3. Height check
height = 68
# if height >= 66 and height <= 72:
#     print("Average height")
66 <= height <= 72

# 4. Temperature comfort
temp = 72
# if temp >= 65 and temp <= 75:
#     print("Perfect weather!")
65 <= temp <= 75

# =============================================================================
# PART 5: SIMPLE GRADE CALCULATOR
# =============================================================================

# Student information
student_name = "Alex"
student_score = 87

# Use chained comparisons for grade ranges:
# A: 90-100, B: 80-89, C: 70-79, F: below 70
if 90 <= student_score <= 100:
    grade = "A"
elif 80 <= student_score <= 89:
    grade = "B"
elif 70 <= student_score <= 79:
    grade = "C"
elif student_score < 70:
    grade = "F"
else:
    grade = "Missing"

print(f"Grade Report:")
# Use ternary for pass/fail status (passing is 70+)


# Print results


# =============================================================================
# WHEN TO USE THESE SHORTCUTS
# =============================================================================

# Use ternary when:
# - Choosing between two simple values
# - Single condition
# - One line is clearer

# Use chained comparisons when:
# - Checking if value is in a range
# - Makes code read like math

# Use regular if-else when:
# - Multiple actions needed
# - Complex conditions
# - Need detailed comments