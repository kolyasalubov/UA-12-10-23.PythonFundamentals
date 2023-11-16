from pyowm import OWM
import config


owm = OWM(config.key)
mgr = owm.weather_manager()

# Search for current weather in London (Great Britain) and get details
city = input("Enter your city")
observation = mgr.weather_at_place(city)
w = observation.weather

def get_weather():
    print(w.detailed_status)         # 'clouds'
    print(f"wind's speed is  {w.wind()['speed']}km/hour")                  # {'speed': 4.6, 'deg': 330}
    print("humidity is: ",w.humidity)                # 87
    print(f"temperature is: {w.temperature('celsius')['temp']}°C")  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    print("rain: ", w.rain)                    # {}
    print("heat index: ", w.heat_index)              # None
    print("clouds: ", w.clouds)                  # 75

get_weather()