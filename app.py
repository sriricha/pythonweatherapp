from tkinter import *
import requests
import json
from datetime import datetime
 
#Initialize Window
root =Tk()
root.geometry("400x400") #default window size
root.resizable(0,0) #to make the window size fixed
root.title("Weather App") #title of our window
 
 
#functions to get and display values
city_value = StringVar()
 
 
def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 

city_value = StringVar()
 
def showWeather():
    api_key = "bf38dc1ee794a48636b6d04fc5d3d976"
 
    #get city name
    city_name=city_value.get()
 
    #API url
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=' + api_key
 
    #url response
    response = requests.get(weather_url)
 
    #changing response from json to python readable 
    weather_info = response.json()
 
    tfield.delete("1.0", "end")   #clear the text field for every new output
 
#if the cod is 200, it means that weather data was successfully fetched
    if weather_info['cod'] == 200:
        kelvin = 273 # value of kelvin
 
 #storing fetched values
        temp = int(weather_info['main']['temp'] - kelvin)                                     #converting default kelvin value to Celcius
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 3.6
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        timezone = weather_info['timezone']
        cloudy = weather_info['clouds']['all']
        description = weather_info['weather'][0]['description']
 
        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)
 
#assigning output values
         
        weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' was not found.\n\tPlease enter a valid city name!"
 
 
 
    tfield.insert(INSERT, weather)#to insert or send value into text field to display output
 
 
#tkinter app
city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10)
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 12 bold').pack()

Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='MediumPurple1', fg='white', activebackground="MediumPurple4", padx=5, pady=5 ).pack(pady= 20)
 
weather_now = Label(root, text = "The Weather is:", font = 'arial 12 bold').pack(pady=10)
 
tfield = Text(root, width=46, height=10)
tfield.pack()
 
root.mainloop()