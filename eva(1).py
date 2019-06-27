from gtts import gTTS
import os
import time
import requests
import json
import pyowm
import weather
from weather import Weather, Unit
import logging
from yahooweather import YahooWeather, UNIT_C

mytext = 'Welcome'
mytext2='this is eva'
print(mytext)
print(mytext2)
language = 'en'
myobj = gTTS(text=mytext, lang=language, slow=False)

os.system("mpg321 w.mp3")
print('choose any of  the following option')
print("""
    1 = Entrance
    2 = Open Parking Space
    """)
opt=int(input('choose - '))
if opt==1:
    print('enter your card')










    print("""
            options-
            1 = access home services
            2 = sos alarm""")
    opt2=int(input('     '))
    if opt2==1:
        print('choose your option')
        print("""
                1 = check water level
                2 = check parking space
                3 = check humidity of your garden
                4 = check weather outside""")
        opt3=int(input('your option  -  '))
        if opt3==1:
            print('please wait .......')
            time.sleep(1)


        elif opt3==2:
            print('please wait .......')
            time.sleep(1)







        elif opt3==3:
            print('please wait ........')
            time.sleep(1)






        elif opt3==4:
            print('please wait ........')
            time.sleep(1)
            send_url = "http://api.ipstack.com/check?access_key=80944066d86f6370d9b7ffa056255ad9"
            geo_req = requests.get(send_url)
            geo_json = json.loads(geo_req.text)
            latitude = geo_json['latitude']
            longitude = geo_json['longitude']
            city = geo_json['city']
            print(latitude,longitude)
            print(city)
            

            logging.basicConfig(level=logging.WARNING)

            yweather = YahooWeather(91543049, UNIT_C)
            if yweather.updateWeather():
                a=("RawData: %s" % str(yweather.RawData))
                b=("Units: %s" % str(yweather.Units))
                c=("Now: %s" % str(yweather.Now))
                d=("Forecast: %s" % str(yweather.Forecast))
                e=("Wind: %s" % str(yweather.Wind))
                f=("Atmosphere: %s" % str(yweather.Atmosphere))
                g=("Astronomy: %s" % str(yweather.Astronomy))

                data = yweather.Now
                print(c)
                print(e)
                print(f)
                print(d)
            else:
                print("Can't read data from yahoo!")
    elif opt2==2:
        print('')
