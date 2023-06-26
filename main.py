import json
import requests
from tkinter import *

city = 'Сочи'
app_id = "79d1ca96933b0328e1c7e3e7a26cb347"
information_oneDay = []
information_fiveDay = []


def WeatherReportOneDay():
    global res
    global data
    global city
    global information_oneDay
    global y
    global x
    city_get = EnterCity.get()
    if city_get != '':
        city = city_get.title()

        EnterCity.delete(0, END)

        Label(window, text=city, font=('Times New Roman', 17, 'bold'), background='#40E0D0').place(x=1, y=50)

        url_ = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid' \
                                                                             '=91f2ab829c963c4a7414b33cd4ee44ad'

        weather_data_ = requests.get(url_).json()

        temperature['text'] = 'Температура сейчас: ' + str(round(weather_data_['main']['temp'])) + '°C'
        temperature.place()
        information_oneDay.append('Температура сейчас: ' + str(round(weather_data_['main']['temp'])) + '°C')
        temperature_feels['text'] = 'Ощущается как: ' + str(round(weather_data_['main']['feels_like'])) + '°C'
        temperature_feels.place()
        information_oneDay.append('Ощущается как: ' + str(round(weather_data_['main']['feels_like'])) + '°C')

        pressure['text'] = 'Давление воздуха: ' + str(round(weather_data_['main']['pressure'] * 0.75)) + ' мм рт с'
        pressure.place()

        information_oneDay.append('Давление воздуха: ' + str(round(weather_data_['main']['pressure'] * 0.75)) + 'мм рт '
                                                                                                                'с')
        humidity['text'] = 'Влажность воздуха(%): ' + str(round(weather_data_['main']['humidity'])) + '%'
        humidity.place()

        information_oneDay.append('Влажность воздуха(%): ' + str(round(weather_data_['main']['humidity'])) + '%')
        wind_speed['text'] = 'Скорость ветра: ' + str(round(weather_data_['wind']['speed'])) + ' м/с'

        res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                           params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
        data = res.json()
        y = 100
        x = 400

        for i in data['list']:
            if y >= 500:
                x = 700
                y = 100
            information_fiveDay.append(str(i['dt_txt']) + ' ' + str('{0:+3.0f}'.format(i['main']['temp'])) + ' ' +
                                       str(i['weather'][0]['description']))
            Label(text=str(i['dt_txt']) + ' ' + str('{0:+3.0f}'.format(i['main']['temp'])) + ' ' + str(
                i['weather'][0]['description']), font=('Times New Roman', 11), background='#40E0D0').place(x=x, y=y)
            y += 20


window = Tk()

window.geometry('990x600')
window.config(background='#40E0D0')

EnterCity = Entry(font=('Times New Roman', 17), width=35, background='#5F9EA0')
EnterCity.place(x=1, y=1)

Button(text='Посмотреть прогноз', font=('Times New Roman', 12), command=WeatherReportOneDay, width=20,
       background='#20B2AA', activebackground='#008B8B').place(x=370, y=0)
Label(text='Прогноз на пять дней', font=('Times New Roman', 17, 'bold'), background='#40E0D0').place(x=400, y=50)

temperature = Label(text='Температура сейчас:', font=('Times New Roman', 15), background='#40E0D0')
temperature.place(x=5, y=100)

temperature_feels = Label(text='Ощущается как:', font=('Times New Roman', 15), background='#40E0D0')
temperature_feels.place(x=5, y=150)

pressure = Label(text='Давление воздуха:', font=('Times New Roman', 15), background='#40E0D0')
pressure.place(x=5, y=200)

humidity = Label(text='Влажность воздуха(%):', font=('Times New Roman', 15), background='#40E0D0')
humidity.place(x=5, y=250)

wind_speed = Label(text='Скорость ветра:', font=('Times New Roman', 15), background='#40E0D0')
wind_speed.place(x=5, y=300)

url = 'https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&lang=ru&appid' \
                                                                    '=91f2ab829c963c4a7414b33cd4ee44ad'

weather_data = requests.get(url).json()
Label(window, text=city, font=('Times New Roman', 17, 'bold'), background='#40E0D0').place(x=1, y=50)

temperature['text'] = 'Температура сейчас: ' + str(round(weather_data['main']['temp'])) + '°C'
temperature.place()
information_oneDay.append('Температура сейчас: ' + str(round(weather_data['main']['temp'])) + '°C')
temperature_feels['text'] = 'Ощущается как: ' + str(round(weather_data['main']['feels_like'])) + '°C'
temperature_feels.place()
information_oneDay.append('Ощущается как: ' + str(round(weather_data['main']['feels_like'])) + '°C')
pressure['text'] = 'Давление воздуха: ' + str(round(weather_data['main']['pressure'] * 0.75)) + ' мм рт с'
pressure.place()
information_oneDay.append('Давление воздуха: ' + str(round(weather_data['main']['pressure'] * 0.75)) + 'мм рт '
                                                                                                       'с')
humidity['text'] = 'Влажность воздуха(%): ' + str(round(weather_data['main']['humidity'])) + '%'
humidity.place()
information_oneDay.append('Влажность воздуха(%): ' + str(round(weather_data['main']['humidity'])) + '%')
wind_speed['text'] = 'Скорость ветра: ' + str(round(weather_data['wind']['speed'])) + ' м/с'

res = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                   params={'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
data = res.json()
y = 100
x = 400
for i in data['list']:
    if y >= 500:
        x = 700
        y = 100
    information_fiveDay.append(str(i['dt_txt']) + ' ' + str('{0:+3.0f}'.format(i['main']['temp'])) + ' ' +
                               str(i['weather'][0]['description']))
    Label(text=str(i['dt_txt']) + ' ' + str('{0:+3.0f}'.format(i['main']['temp'])) + ' ' + str(
        i['weather'][0]['description']), font=('Times New Roman', 11), background='#40E0D0').place(x=x, y=y)
    y += 20
weatherDataStructure = json.dumps(weather_data, indent=2)
print(information_oneDay)

window.mainloop()
