#!/usr/bin/python
import pyowm
 
owm = pyowm.OWM('cce458d50052bfe66f9df1bb019c10ca')
observation = owm.weather_at_place('Cape Coast')
w = observation.get_weather() 
print(w.get_wind()['speed'])
#print(w.get_humidity())
#print(w.get_temperature()['temp'])

