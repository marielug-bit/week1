from collections import defaultdict

from pyowm.owm import OWM
from pyowm.utils import timestamps

owm = OWM('5766c150f3825b8853309723ebf0a98f')
weather_mgr = owm.weather_manager()
observation = weather_mgr.weather_at_place('Paris,FR')  # the observation object is a box containing a weather object
#weather = observation.weather
#print(weather.humidity)

forecast = weather_mgr.forecast_at_place("Paris,FR", '3h')
for weather in forecast.forecast:
     print(weather.reference_time('date'), weather.humidity)

daily_humidity = defaultdict(list)
humidity_list = []


for weather in forecast.forecast:
    
    date = weather.reference_time('date').date()   # récupérer seulement le jour
    humidity = weather.humidity
    
    daily_humidity[date].append(humidity)

# calcul moyenne humidité par jour
for day, values in list(daily_humidity.items())[:3]:
    
    avg_humidity = sum(values) / len(values)
    humidity_list.append(avg_humidity)
    
    print(f"{day} → {round(avg_humidity)}%")


days = ['Day 1', 'Day 2', 'Day 3']

    