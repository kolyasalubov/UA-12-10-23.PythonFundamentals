from pyowm import OWM


def get_weather(city):
    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    weather = observation.weather
    return weather


