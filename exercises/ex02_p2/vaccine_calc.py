"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730407394"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    final = days_to_target(population, doses, doses_per_day, target)
    final_2 = future_date(final)
    print("We will reach " + str(target) + "% vaccination in " + str(final) + " days, which falls on " + final_2 + ".")


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Calculate days to target goal."""
    percent = target * .01
    goal_administered = percent * population
    doses = doses / 2
    population_left = goal_administered - doses
    days = population_left / doses_per_day
    days = float(days * 2)
    days = round(days)
    return days


def future_date(days_left: int) -> str:
    """Find future date."""
    today: datetime = datetime.today()
    fortnight: timedelta = timedelta(days_left)
    future: datetime = today + fortnight
    days_left = str(days_left)
    return future.strftime("%B %d, %Y")


if __name__ == "__main__":
    main()
