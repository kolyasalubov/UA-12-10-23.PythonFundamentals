class Weather:
    from pyowm import OWM

    API_KEY = 'ef2206ff5da67de63306d0b143e20872'

    # ---------- FREE API KEY examples ---------------------

    def get_weather(self, country):
        owm = self.OWM(self.API_KEY)
        mgr = owm.weather_manager()

        observation = mgr.weather_at_place(str(country))
        w = observation.weather
        self.result = {
            'status': w.detailed_status,
            'wind': w.wind(),
            'humidity': w.humidity,
            'temperature': w.temperature('celsius'),
            'rain': w.rain,
            'heat_index': w.heat_index,
            'clouds': w.clouds
        }

