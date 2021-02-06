"""A vaccination calculator."""

__author__ = "730407394"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


population: int = int(input("Population: "))
doses_administered: int = int(input("Doses Administered: "))
doses_per_day: float = float(input("Doses Per Day: "))
target_percent: int = int(input("Target Percent Vaccinated: "))
percent = target_percent * .01
goal_administered = percent * population
doses_administered = doses_administered / 2.0
population_left = goal_administered - doses_administered
days = population_left / doses_per_day
days = float(days * 2)
days = round(days)
today: datetime = datetime.today()
one_day: timedelta = timedelta(1)
tomorrow: datetime = today + one_day
fortnight: timedelta = timedelta(days)
future: datetime = today + fortnight
days = str(days)
target_percent = str(target_percent)
print("We will reach " + target_percent + "% vaccination in " + days + " days, which falls on " + future.strftime("%B %d, %Y") + ".")
