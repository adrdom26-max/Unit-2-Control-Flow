text = "hello"
vowels = "aeiouAEIOU"
count = 0
for char in text:
    if char in vowels:
        count += 1
    print(count)

while True:
    number = int(input("User Enter: "))
    if number < 0:
        break
    else: 
        sum += number
    print(sum)

for row in range(3):
    for col in range(4):
        print("*", end=" ")
    print()
