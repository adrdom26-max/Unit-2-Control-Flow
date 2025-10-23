# Simple 3x3
# for row in range(3):
#     for col in range(3):
#         # print("hello")
#         print("hello", end=" ")
#     print()

# for row in range(4):
#     for col in range(5):
#         print("⭐", end=" ")
#     print()

# Numbers 
# for row in range(3):
#     for col in range(3):
#         print(f"({row}, {col})" , end=" ")
#     print()

# Triangle Ascending

# for row in range(5):
#     for col in range(row + 1):
#         print(f"({row},{col})", end=" ")
    # print()

# for row in range(5,0,-1):
#     for col in range(row):
#         print(f"⭐", end=" ")
#     print()

# 3x3 Multiplication
for row in range(1,4):
    for col in range(1,4):
        product = row * col
        print(f"{product:3}", end=" ")
    print()