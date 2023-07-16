from datetime import date

# a function that take the current date and add a number of years to it.
def add_years_to_date(original_date : date, years_to_add : int):

    # replace the year of the original date with the year of the original date plus the number of years to add
    result = original_date.replace(year=original_date.year + years_to_add)
    return result

# check if the tire wear is greater than 90% for any of the tires
def check_carrigan_tire_wear(tire_wear : int):
    for tire_wear_value in tire_wear:
        if tire_wear_value > 0.9:
            return True
    return False

# check if the sum of the tire wear is greater than 3
def check_octoprime_tire_wear(tire_wear : int):
    return sum(tire_wear) >= 3

'''

from datetime import date

def add_years_to_date(original_date, years_to_add):
    result = original_date.replace(year=original_date.year + years_to_add)
    return result

# Example usage
original_date = date(2022, 7, 14)
years_to_add = 5

new_date = add_years_to_date(original_date, years_to_add)
print(f"Original Date: {original_date}")
print(f"New Date after adding {years_to_add} years: {new_date}")

'''