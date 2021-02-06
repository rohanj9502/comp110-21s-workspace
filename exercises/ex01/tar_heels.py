"""An exercise in remainders and boolean logic."""

__author__ = "730407394"


number: int=int(input("Enter an int: "))

if number%2==0 and number%7==0:
    print("TAR HEELS")
else:
    if number%2==0 and number%7!=0:
        print("TAR")
    else:
        if number%2!=0 and number%7==0:
            print("HEELS")
        else:
            print("CAROLINA")