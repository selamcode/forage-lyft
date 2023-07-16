from datetime import date

# a function that take the current date and add a number of years to it.
def add_years_to_date(original_date : date, years_to_add : int):

    # replace the year of the original date with the year of the original date plus the number of years to add
    result = original_date.replace(year=original_date.year + years_to_add)
    return result
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