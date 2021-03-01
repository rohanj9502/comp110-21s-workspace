"""You can keep playing blackjack with a continious point count."""

from random import randint

__author__ = "730407394"


def main() -> None:
    """Entry into program."""
    greet()
    option: str = str(input("What would you like to do: Play, Exit, Check Score, or Talk to the Dealer? "))
    print(three_options(option))


def greet() -> None:
    """Ask their name."""
    player = str(input("What is your name? "))
    print(f"Hi {player}, are you ready to play blackjack!")


def three_options(option: str) -> str:
    """Asks their choice."""
    if option == "Exit":
        return f"Good bye! You ended with {points} points {SMILEY_FACE}."
    else:
        if option == "Play":
            game()
        else: 
            if option == "Check Score":
                return point_talk(points)
            else:
                if option == "Talk to the Dealer":
                    dealer_talk()


def point_talk(x: int) -> str:
    """Dialogue about points."""
    global points
    if points == 1:
        print(f"You have {points} point.")
    else:
        print(f"You have {points} points.")
    option: str = str(input("What would you like to do now: Play, Exit, or Talk to the Dealer? "))
    print(three_options(option))
    

def dealer_talk() -> None:
    """Talk to the dealer."""
    global points
    chips: int = points * 500
    age: int = int(input("Hey, how old are you? "))
    if age < 21:
        print("Woah, you are way too young! It's ok though, I'll let it slide.")
    else:
        print("Good, thats the legal age.")
    question: str = str(input("Would you like to know how many chips you have? "))
    if question == "Yes":
        print(f"You have {chips} chips.")
    if question == "No":
        print("That is rude!")
    option: str = str(input("What would you like to do now: Play, Exit, or Check Score? "))
    print(three_options(option))


def game() -> None:
    """A game."""
    global points
    my_card1: int = randint(1, 10)
    my_card2: int = randint(1, 10)
    my_card3: int = randint(1, 10)
    my_card4: int = randint(1, 10)
    my_card5: int = randint(1, 10)
    dealer1: int = randint(1, 10)
    dealer2: int = randint(1, 10)
    dealer3: int = randint(1, 10)
    dealer4: int = randint(1, 10)
    dealer5: int = randint(1, 10)
    mysum: int = my_card1 + my_card2
    print(f"I have dealt two cards. You have cards with values of {my_card1} and {my_card2}. Your total is {mysum}.")
    hit1: str = str(input("Do you hit or stand? "))
    if hit1 == "Hit":
        mysum += my_card3
        print(f"Your third card is {my_card3} for a total of {mysum}.")
        if mysum == 21:
            print("You got blackjack!!! I have added a point for you.")
            points += 1
        if mysum > 21:
            print("You busted!!!")
        if mysum < 21:
            hit2: str = str(input("Do you hit or stand now? "))
            if hit2 == "Hit":
                mysum += my_card4
                print(f"Your fourth card is {my_card4} for a total of {mysum}.")
                if mysum == 21:
                    print("You got blackjack!!! I have added a point for you.")
                    points += 1
                if mysum > 21:
                    print("You busted!!!")
                if mysum < 21:
                    hit3: str = str(input("Do you hit or stand now? "))
                    if hit3 == "Hit":
                        mysum += my_card5
                        if mysum == 21:
                            print("You got blackjack!!! I have added a point for you.")
                            points += 1
                        if mysum > 21:
                            print("You busted!!!")
    if mysum < 21:
        if hit1 or hit2 or hit3 == "Stand":
            dealersum: int = dealer1 + dealer2
            print(f"Ok your total is {mysum}. Now I will get my cards.")
            print(f"My cards are {dealer1} and {dealer2} and my total is {dealersum}.")
            if dealersum < 16:
                dealersum += dealer3
                print(f"I will add another card. My third card is {dealer3} and my total is {dealersum}.")
                if dealersum < 16:
                    dealersum += dealer4
                    print(f"I will add another card. My fourth card is {dealer4} and my total is {dealersum}.")
                    if dealersum < 16:
                        dealersum += dealer5
                        print(f"I will add another card. My fifth card is {dealer5} and my total is {dealersum}.")
            if dealersum > 21:
                print("I busted!! I will give you a point.")
                points += 1
            if dealersum > 15:
                if dealersum < 22:
                    print(f"Ok I stand at {dealersum}")
                    if mysum > dealersum:
                        print("Oh! You beat me!! I will give you a point.")
                        points += 1
                    else:
                        if mysum == dealersum:
                            print("We tied.")
                        else:
                            if mysum < dealersum:
                                print("You lost to me. Better luck next time!")
    replay: str = str(input("What do you want to do? Play again, Exit, Talk to the Dealer, or Check Score? "))
    if replay == "Play again":
        game()
    else: 
        if replay == "Exit":
            print(f"Good bye! You ended with {points} points {SMILEY_FACE}.")
        else:
            if replay == "Talk to the Dealer":
                dealer_talk()
            else:
                point_talk(points)


points: int = 0
player: str
SMILEY_FACE = "\U0001f600"


if __name__ == "__main__":
    main()