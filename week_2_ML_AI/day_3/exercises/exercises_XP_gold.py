import datetime
import holidays

def display_today_s_date():
    today = datetime.date.today()
    israeli_holidays = holidays.US()

    future_holidays = [holiday for holiday in israeli_holidays if holiday - today > 0]
    
    next_holiday = min(future_holidays)
    print(f'today date is {today}, next holiday is {next_holiday} in {(next_holiday-today).days} days')

display_today_s_date()


def age_on_planets(age_in_seconds):
    EARTH_YEAR_SECONDS = 31557600

    orbital_periods = {
        "Earth": 1,
        "Mercury": 0.2408467,
        "Venus": 0.61519726,
        "Mars": 1.8808158,
        "Jupiter": 11.862615,
        "Saturn": 29.447498,
        "Uranus": 84.016846,
        "Neptune": 164.79132,
    }

    for planet, period in orbital_periods.items():
        age = age_in_seconds / (EARTH_YEAR_SECONDS * period)
        print(f"{planet}: {age:.2f} years")

    
    import re

def return_numbers(text):
    return ''.join(re.findall(r'\d', text))