"""EX03 - prime functions."""

__author__: str = "730407394"


def main() -> None:
    """Entrypoint of the program."""
    print(is_prime(0))
    print(is_prime(6))
    print(is_prime(31))
    print(is_prime(110)) 
    print(list_primes(-1, 5))   


def is_prime(x: int) -> bool:
    """Is the number prime?"""
    divider: int = 2
    if x < 2:
        return False
    while divider < x + 1:
        remainder = x % divider
        if divider == x:
            return True
        else:
            if remainder != 0:
                divider += 1
            if remainder == 0:
                return False


def list_primes(x: int, y: int) -> list[int]:
    """Makes a list of primes."""
    a = []
    while x < y:
        prime_check = is_prime(x)
        if prime_check is True:
            a.append(x)
            x += 1
        if prime_check is False:
            x += 1
    return a


if __name__ == "__main__":
    main()