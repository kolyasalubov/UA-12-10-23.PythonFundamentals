from pyowm import OWM


API_KEY = 'c681c28434f69b999b35eefa39c20239'
# ---------- FREE API KEY examples ---------------------



def get_weather(city):
# Search for current weather in London (Great Britain) and get details
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    return w

if __name__ == '__main__' :
    w = get_weather('Київ')
    print(w.detailed_status)         # 'clouds'
    print(w.wind())                  # {'speed': 4.6, 'deg': 330}
    print(w.humidity)                # 87
    print(w.temperature('celsius'))  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
    print(w.rain)                    # {}
    print(w.heat_index)              # None
    print(w.clouds)                  # 75