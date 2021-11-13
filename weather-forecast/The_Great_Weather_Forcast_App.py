import tkinter as tk
from tkinter import font
import requests

HEIGHT = 700
WIDTH = 800

def format_response(resp):
    print(resp)
    try:
        name = resp["name"]
        desc = resp['weather'][0]['description']
        speed = resp['wind']['speed']
        temp = resp['main']['temp']
        mintemp = resp['main']["temp_min"]
        msg = "City: %s \nWeather Condition: %s \nTemprature (°C): %s \nMinimum Temprature: %s \nWind Speed(km\hr)  : %s " % (name, desc, temp, mintemp, speed)
    except:
        msg = "Please provide a valid city name"

    return(msg)

def get_weather(city):
    api_key = "08c89c87e31eaf144223f16721ae38ab"
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {"AppId": api_key, "q": city, "units": "imperial"}
    response = requests.get(url, params=params)
    resp  = response.json()

    label["text"] = format_response(resp)


root = tk.Tk()
root.geometry('500x300')
img = tk.PhotoImage(file="background.png")
label = tk.Label(root,image=img)
label.place(relwidth=1, relheight=1)
button = tk.Button(root, text="Get Weather Results", font="Serif", bg="orange", fg="black", command=lambda: get_weather(entry.get()))

label = tk.Label(root, font=("Comic Sans MS", 13))

entry = tk.Entry(root, bg="red", fg="white", font=("Helvetica", 15))
label.place(relx= 0.1, rely=0.3, relwidth=0.8, relheight=0.9)
entry.grid(row=0, column=0)
button.grid(row=0, column=1)
root.mainloop()
