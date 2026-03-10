from pyowm.owm import OWM
from pyowm.utils import timestamps
owm = OWM('5766c150f3825b8853309723ebf0a98f')
weather_mgr = owm.weather_manager()
observation = weather_mgr.weather_at_place('Paris,FR')  # the observation object is a box containing a weather object
weather = observation.weather
weather.status           # short version of status (eg. 'Rain')
weather.detailed_status  # detailed version of status (eg. 'light rain')
wind_dict_in_meters_per_sec = observation.weather.wind()
wind_dict_in_meters_per_sec['speed']
wind_dict_in_meters_per_sec['deg']
#wind_dict_in_meters_per_sec['gust']

sunrise_unix = weather.sunrise_time(timeformat='date')
sunrset_unix = weather.sunset_time(timeformat='date')  # default unit: 'unix'

print(f'''Hi, current weather in Paris : {weather.status } \n
current wind in Paris : speed of {wind_dict_in_meters_per_sec['speed']} ... \n
sunrise hour : {sunrise_unix}
sunrset hour : {sunrset_unix}''')

place_input = input('Where do you want information on the weather? ')
reg = owm.city_id_registry()
list_of_tuples = london = reg.ids_for(place_input, matching='exact')
a,b,c,d,e,f = list_of_tuples[0]
place = f"{b},{c}"
observation = weather_mgr.weather_at_place(place)  # the observation object is a box containing a weather object
weather = observation.weather
weather.status           # short version of status (eg. 'Rain')
weather.detailed_status  # detailed version of status (eg. 'light rain')
wind_dict_in_meters_per_sec = observation.weather.wind()
wind_dict_in_meters_per_sec['speed']
wind_dict_in_meters_per_sec['deg']
#wind_dict_in_meters_per_sec['gust']

print(f'''Hi, current weather in {place} : {weather.status } \n
current wind in {place} : speed of {wind_dict_in_meters_per_sec['speed']} ... \n
sunrise hour : {sunrise_unix}
sunrset hour : {sunrset_unix}''')

forecast = weather_mgr.forecast_at_place("Paris,FR", "3h") #
print(type(forecast))
forecast_list = forecast.forecast.weathers
print(forecast_list)

for weather in forecast_list:
    print(weather.reference_time('iso'))
    print(weather.temperature('celsius')['temp'])


mgr = owm.airpollution_manager()


# Get available CO Index in the last 24 hours
air = mgr.air_quality_at_coords(31.7683, 35.2137)
    
print("AQI:", air.aqi)
print()

#print("Components:", air.components)

