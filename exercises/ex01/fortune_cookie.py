"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730407394"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


x: int = int ((randint(1, 4)))
print("Your fortune cookie says...")
if x == 1:
    print("A beautiful, smart, and loving person will be coming into your life.")
else:
    if x == 2:
        print("Your life will be happy and peaceful.")
    else:
        if x == 3:
            print("Soon life will become more interesting.")
        else:
            print("You will receive good news soon!")
print("Now, go spread positive vibes!")