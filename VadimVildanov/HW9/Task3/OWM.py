from pyowm import OWM


API_KEY = 'ef2206ff5da67de63306d0b143e20872'
# ---------- FREE API KEY examples ---------------------


def get_weather(city):
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place('London,GB')
    weather = observation.weather
    return weather


if __name__ == "__main__":
    w = get_weather("Kyiv")
    print(w.detailed_status)         # 'clouds'
    print(w.wind())                  # {'speed': 4.6, 'deg': 330}
    print(w.humidity)                # 87
    print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    print(w.rain)                    # {}
    print(w.heat_index)              # None
    print(w.clouds)                  # 75



