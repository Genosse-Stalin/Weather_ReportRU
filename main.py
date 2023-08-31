import json
import requests
from tkinter import *

city = 'Сочи'
app_id = "edb13ef869842c8a83c691c532ecedf0"
information_oneDay = []
tempMin_fiveDay = []
tempMax_fiveDay = []
weather_fiveDay = []
weather_icon = []


def WeatherReportOneDay():
    pass


#     global res
#     global data
#     global city
#     global information_oneDay
#     global y
#     global x
#     city_get = EnterCity.get()
#     if city_get != '':
#         city = city_get.title()
#
#         EnterCity.delete(0, END)
#         sityLable['text'] = city
#         sityLable.place(x=1, y=50)


window = Tk()

window.geometry('600x950')
window.config(background='#40E0D0')

EnterCity = Entry(font=('Times New Roman', 17), width=35, background='#5F9EA0')
EnterCity.place(x=1, y=1)

Button(text='Посмотреть прогноз', font=('Times New Roman', 12), command=WeatherReportOneDay, width=20,
       background='#20B2AA', activebackground='#008B8B').place(x=370, y=0)

url = 'https://api.openweathermap.org/data/2.5/weather'
      # 'q=' + city + '&units=metric&lang=ru&appid' \
      #                                                               '=edb13ef869842c8a83c691c532ecedf0'

url2 = 'https://api.openweathermap.org/data/2.5/forecast?q=' + city + '&units=metric&lang=ru&appid' \
                                                                      '=edb13ef869842c8a83c691c532ecedf0'

weather_data = requests.get(url, 'q=' + city + '&units=metric&lang=ru&appid=edb13ef869842c8a83c691c532ecedf0').json()

print(weather_data)
cityLabel = Label(window, text=city, font=('Times New Roman', 30, 'bold'), background='#40E0D0')
cityLabel.place(x=1, y=50)
weather_5day = requests.get(url2).json()
print(weather_5day)
j = 5

x = 10
y = 100

for i in range(30):
    l = Label(window, font=('Times New Roman', 17, 'bold'), background='#40E0D0')
    l.place(x=x, y=y)
    information_oneDay.append(l)
    y += 50

information_oneDay[0]['text'] = f"Погодное явление: {weather_data['weather'][0]['description']}"
information_oneDay[1]['text'] = f"Температура: {round(weather_data['main']['temp'])}°C"
information_oneDay[2]['text'] = f"Ощущается как: {round(weather_data['main']['feels_like'])}°C"
information_oneDay[3]['text'] = f"Видимость: {round(weather_data['visibility'])}м"
information_oneDay[4]['text'] = f"Скорость ветра: {round(weather_data['wind']['speed'])}м/с"

for i in weather_5day['list']:
    tempMin_fiveDay.append(round(i['main']['temp_min']))
    tempMax_fiveDay.append(round(i['main']['temp_max']))
    weather_fiveDay.append(i['weather'][0]['description'])
    weather_icon.append(i['weather'][0]['icon'])

for i in range(5, 13):
    information_oneDay[i]['text'] = tempMin_fiveDay[i]
    information_oneDay[i + 8]['text'] = tempMax_fiveDay[i]
    information_oneDay[i]['font'] = ('Times New Roman', 13, 'bold')
    information_oneDay[i + 8]['font'] = ('Times New Roman', 13, 'bold')
    information_oneDay[i + 16]['font'] = ('Times New Roman', 13, 'bold')
    information_oneDay[i].place(y=370, x=x)
    information_oneDay[i + 8].place(y=390, x=x)
    information_oneDay[i + 16].place(y=350, x=x)
    x += 50

window.mainloop()
