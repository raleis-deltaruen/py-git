# 1.generate a random number and save it into a variable
# 2.Welcome user and ask for their guess
# 3.Save user input into a variable
# 4.Compare my variable to user variable
# 5.Print the result
import sys

a = 10
if len(sys.argv) == 2:
    a = int(sys.argv[-1], base=10)

if not f"{a}".isdigit() or a < 2:
    print("Error: invalid parameter. It should be an integer value and > 1")
    exit()

raw_user_input = input(f"pick a number from 1-{a}: ")
user_input = int(raw_user_input, base=10)

from random import randint
random_number = randint(1, a)
if user_input == random_number:
    print("you guessed the number!!!!!") 
else:
    print("try again!")
    print(f"{random_number} was the correct number")