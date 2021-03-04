#Website for API     https://openweathermap.org/api

from tkinter import *
from tkinter import messagebox
from configparser import ConfigParser
import requests

url='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'

config_file='config.ini'
config=ConfigParser()
config.read(config_file)
api_key=config['api_key']['key']

def get_weather(city):
    result=requests.get(url.format(city, api_key))
    if result:
        json=result.json()
        city=json['name']
        country=json['sys']['country']
        temp_kelvin=json['main']['temp']
        temp_celcius=temp_kelvin-273.15
        temp_farhenheit=(temp_kelvin -273.15)*9/5 +32
        icon=json['weather'][0]['icon']
        weather=json['weather'][0]['main']
        final=(city, country, temp_celcius, temp_farhenheit, icon, weather)
        return final
    else:
        return None

def search():
    city=city_text.get()
    weather=get_weather(city)
    if weather:
        location_lbl['text']='{}, {}'.format(weather[0], weather[1])
        img["file"]='weather\\{}.png'.format(weather[4])
        temp_lbl['text']='{:.2f}C, {:.2f}F'.format(weather[2], weather[3])
        weather_lbl['text']=weather[5]
    else:
        messagebox.showerror('Error', 'Cannot find city {}'.format(city))

def reset():
    city_text.set("")
    location_lbl['text']=""
    temp_lbl['text']=""
    image['image']=""
    temp_lbl['text']=""
    weather_lbl['text']=""


app=Tk()
app.title("Weather App")
app.geometry('400x600')
app.configure(bg="fuchsia")

name_lbl=Label(app, text='LIVE WEATHER', font=('bold', 30), bg="darkblue", fg="white")
name_lbl.pack(pady=5)

city_text=StringVar()
city_entry=Entry(app, textvariable=city_text, font=('bold', 20), bg="lime")
city_entry.pack(pady=15)

search_btn=Button(app, text='Search Weather', font=('bold', 25), width=12, bg='black', fg="white", command=search)
search_btn.pack(pady=5)

location_lbl=Label(app, text='', font=('bold', 20), bg="Red", fg="white")
location_lbl.pack(pady=5)

img=PhotoImage(file="")
image=Label(app, image=img, bg="blue")
image.pack(pady=5)

temp_lbl=Label(app, text='', font=('bold', 15), bg="gold")
temp_lbl.pack(pady=5)

weather_lbl=Label(app, text='', font=('bold', 15), bg="orangered", fg="white")
weather_lbl.pack(pady=5)

reset_btn=Button(app, text='Reset City', font=('bold', 25), width=12, bg='black', fg="white", command=reset)
reset_btn.pack(pady=5)

app.mainloop()