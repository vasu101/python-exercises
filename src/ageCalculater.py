from datetime import date

def year_turns_100(age: int) -> int:
    """Return the calendar year when the user will turn 100."""
    current_year = date.today().year
    return current_year + (100 - age)

name = input("What is your name? ")
age = int(input("How old are you? "))

year = year_turns_100(age)
message = f"{name}, you will turn 100 years old in the year {year}."

print(message)
