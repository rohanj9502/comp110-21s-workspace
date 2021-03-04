"""EX03 - palindromify function."""

__author__: str = "730407394"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time ", False))


def palindromify(x: str, y: bool) -> str:
    """Palindromify's a number."""
    if y is True:
        i = len(x) - 1
        a = list(x)
        while i > -1:
            a.append(a[i])
            i -= 1
    if y is False:
        i = len(x) - 2
        a = list(x)
        while i > -1:
            a.append(a[i])
            i -= 1
    str1: str = "".join(a)
    return str1


if __name__ == "__main__":
    main()