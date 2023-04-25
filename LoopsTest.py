secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
number = 777


while number != 777:
    if number < 777 or number > 777:
        print("Ha ha! You're stuck in my loop!")
        number = int(input("Enter an Integer Number :"))
#   elif number > 777:
#        print("Ha ha! You're stuck in my loop....!")
#        number = int(input("Enter an Integer Number :"))
    if number == 777:
        print(number, "Well done, muggle! You are free now.")

