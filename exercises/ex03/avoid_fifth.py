"""EX03 - avoid_fifth function."""

__author__: str = "730407394"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("hello"))
    print(avoid_fifth("Easer"))


def avoid_fifth(x: str) -> str:
    """Takes out the letter e."""
    i: int = 0
    a = list(x)
    length = len(x)
    while i < length:
        if a[i] == "e":
            a.pop(i)
            length -= 1
        else:
            if a[i] == "E":
                a.pop(i)
                length -= 1
            else:
                i += 1
    str1 = "".join(a)
    return str1


if __name__ == "__main__":
    main()