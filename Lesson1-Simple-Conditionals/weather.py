# Unit 2 Lesson 1 Homework: Weather Advisory System
# Name: ___________________
# Date: ___________________

print("Weather Advisory System")
print("=" * 23)

# Step 1: Get weather information from user
# TODO: Get temperature as integer
temperature = int(input("Temperature in degrees:"))

# TODO: Get sunny status and convert to boolean
weather = str(input("It is sunny:"))
is_sunny = sunny_input == "yes"
# Step 2: Display weather report
print(f"\nWeather Report:")
# TODO: Show temperature and sunny status
print("-" * 18)
print(f"Temperature: {temperature}")
print(f"Sunny: {'Yes' if is_sunny else 'No'}")
# Step 3: Temperature advice
# TODO: Use if-else to give clothing advice based on temperature
if temperature >= 75:
    print("Wear shorts and a t-shirt")
else:
    print("Wear hoodie and sweats")
# Step 4: Activity suggestions  
# TODO: Use if-else to suggest activities based on sunny status
if is_sunny:
    print("It's a great day to go outside!")
else:
    print("Stay inside and read")
print("\nStay safe and have fun!")