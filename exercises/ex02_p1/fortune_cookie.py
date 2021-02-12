"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730407394"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")


def fortune_cookie() -> str:
    """Gives a fortune!"""
    x: int = int((randint(1, 4)))
    if x == 1:
        return "A beautiful, smart, and loving person will be coming into your life."
    else:
        if x == 2:
            return "Your life will be happy and peaceful."
        else:
            if x == 3:
                return "Soon life will become more interesting."
            else:
                return "You will receive good news soon!"


# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()
