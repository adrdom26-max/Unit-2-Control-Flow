# Three Logical Operators
# and (Both conditions must be true)
# or (at least one condition must be true)
# not (flips true/false)

# Example - Game Access Control 
# take user inputs - as booleans

# take user inputs - as strings
player_level = input(("Enter your player level:"))
has_premium = input(("Do you have premium account?(0/1)):"))
is_banned = input(("Are your currently banned?(0/1)):"))

if has_premium == "yes":
    has_premium = True
elif has_premium == 'no':
    has_premium = False
else:
    print("Invalid has_premium")

    
if is_banned == "yes":
    is_banned = True
elif is_banned == 'no':
    is_banned = False
else:
    print("Invalid is_banned")


# Access control logic
can_access_game = not is_banned and (player_level >= 10 or has_premium)
can_access_premium_features = not is_banned and has_premium
can_join_tournaments = not is_banned and player_level >= 25 and has_premium
# print access details
print(f"Player Level: {player_level}")
print(f"Premium: {has_premium}")
print(f"Banned: {is_banned}")
print(f"*"*25)
print(f"Can access game: {can_access_game}")
print(f"Can access premium features: {can_access_premium_features}")
print(f"Can join tournaments: {can_join_tournaments}")

# Logical Operator Precedence
#1 not(highest)
#2 and
#3 (lowest)

print(not False or False and True)