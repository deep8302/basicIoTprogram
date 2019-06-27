import pyowm

owm = pyowm.OWM('5304fa933d98ccbc60cec32e958937b4')
observation = owm.weather_at_place("Cambridge,uk")
w = observation.get_weather()
temperature = w.get_temperature('celsius')
tomorrow = pyowm.timeutils.tomorrow()
wind = w.get_wind()
print(w)
print(wind)
print(temperature)
print(tomorrow)
