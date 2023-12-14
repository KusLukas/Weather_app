import requests, json
import time
from tkinter import *
from PIL import Image
from io import BytesIO

class Weather:

    def __init__(self,weather_type,city_name):
        api_key = 'c2b22ee66e1d60f7ad6bb347c3ecb743'
        base_url = "http://api.openweathermap.org/data/2.5/"
        #city_name = input("Enter city name : ")
        complete_url = base_url + weather_type + '?' + "q=" + city_name  + "&appid=" + api_key
        response = requests.get(complete_url)
        weather_data = response.json()
        self.weather_data=weather_data

    def Current(self):

        if self.weather_data["cod"] == "404":
            self.popupmsg(" City Not Found ")

        elif self.weather_data["cod"]==401:
            self.popupmsg("Invalid API key")

        else:
            # print(self.weather_data)
            weather_main = self.weather_data["main"]
            self.current_temperature = weather_main["temp"]
            self.feel_temperature = weather_main["feels_like"]
            self.min_temperature = weather_main["temp_min"]
            self.max_temperature = weather_main["temp_max"]
            self.current_pressure = weather_main["pressure"]
            self.current_humidiy = weather_main["humidity"]
            weather_sky = self.weather_data["weather"]
            self.weather_description = weather_sky[0]["description"]
            self.calc_time=time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(self.weather_data["dt"]))
            local_stuff=self.weather_data["sys"]
            self.sunrise=time.strftime("%H:%M:%S", time.localtime(local_stuff["sunrise"]))
            self.sunset=time.strftime("%H:%M:%S", time.localtime(local_stuff["sunset"]))
            self.location=self.weather_data["name"]
            self.country=local_stuff["country"]
            icon_id=weather_sky[0]['icon']
            self.icon=Image.open(BytesIO(requests.get('http://openweathermap.org/img/w/{}.png'.format(icon_id)).content))
            # print(" Temperature = " +
            #                 str(round(current_temperature- 273.15,2))+u"\u00b0C" +
            #       "\n atmospheric pressure = " +
            #                 str(current_pressure)+"hPa" +
            #       "\n humidity = " +
            #                 str(current_humidiy)+"%" +
            #       "\n description = " +
            #                 str(weather_description))
        return self

    def popupmsg(self,msg):
        popup = Tk()
        popup.wm_title("Error")
        label = Label(popup, text=msg)
        label.pack(side="top", fill="x", pady=10)
        B1 = Button(popup, text="Darn it!!!", command = popup.destroy)
        B1.pack()
        popup.mainloop()

    def Forecast_five_d(self):

        if self.weather_data["cod"] == "404":
            self.popupmsg(" City Not Found ")

        elif self.weather_data["cod"]==401:
            self.popupmsg("Invalid API key")

        else:
            self.current_temperature=[]
            self.feel_temperature=[]
            self.min_temperature=[]
            self.max_temperature=[]
            self.current_pressure=[]
            self.current_humidiy=[]
            self.wind=[]
            self.weather_description=[]
            self.calc_time=[]
            self.sunrise=[]
            self.sunset=[]
            icon_id=[]
            self.icon=[]

            for time_l in self.weather_data['list']:
                #print(time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime(time_l['dt'])))
                #print( self.weather_data)

                weather_main = time_l["main"]
                self.current_temperature.append(weather_main["temp"])
                self.feel_temperature.append(weather_main["feels_like"])
                self.min_temperature.append(weather_main["temp_min"])
                self.max_temperature.append(weather_main["temp_max"])
                self.current_pressure.append(weather_main["pressure"])
                self.current_humidiy.append(weather_main["humidity"])
                weather_sky = time_l["weather"]
                self.wind.append(time_l['wind']['speed'])
                self.weather_description.append(weather_sky[0]["description"])
                self.calc_time.append(time.strftime("%b %d %H", time.localtime(time_l["dt"])))
                local_stuff=self.weather_data["city"]
                self.sunrise.append(time.strftime("%H:%M:%S", time.localtime(local_stuff["sunrise"])))
                self.sunset.append(time.strftime("%H:%M:%S", time.localtime(local_stuff["sunset"])))
                self.location=local_stuff["name"]
                self.country=local_stuff["country"]


            # print(" Temperature = " +
            #                 str(round(current_temperature- 273.15,2))+u"\u00b0C" +
            #       "\n atmospheric pressure = " +
            #                 str(current_pressure)+"hPa" +
            #       "\n humidity = " +
            #                 str(current_humidiy)+"%" +
            #       "\n description = " +
            #                 str(weather_description))
        return self
