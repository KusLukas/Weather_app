from weather_request import Weather
from multicolor_labels import multicolor_ylabel, multicolor_ylabel_double_ax
from tkinter import *
from PIL import Image, ImageTk
from time import strptime
import datetime
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator


class interface:
    def __init__(self):
        main = Tk()
        main.title("Weather app beta")
        #main.geometry("950x40")
        self.main=main

        time = Label(main)
        time.grid(row=0,column=0,columnspan =6)
        self.time=time

        self.frame_displayboxex = Frame(self.main, bg='lightgreen')
        self.frame_displayboxex.grid(row=2,column=3,sticky='e')
        self.weather_gui()

    def cb_check(self):
        if self.temp_true.get() and self.temp_feel_true.get() and self.press_true.get():
            self.wind_button.config(state=DISABLED)
            self.hum_button.config(state=DISABLED)
        elif self.temp_true.get() and self.temp_feel_true.get() and self.wind_true.get():
            self.press_button.config(state=DISABLED)
            self.hum_button.config(state=DISABLED)
        elif self.temp_true.get() and self.temp_feel_true.get() and self.humidity_true.get():
            self.press_button.config(state=DISABLED)
            self.wind_button.config(state=DISABLED)
        elif self.press_true.get() and self.humidity_true.get():
            self.temp_button.config(state=DISABLED)
            self.tempfeel_button.config(state=DISABLED)
            self.wind_button.config(state=DISABLED)
        elif self.wind_true.get() and self.humidity_true.get():
            self.press_button.config(state=DISABLED)
            self.temp_button.config(state=DISABLED)
            self.tempfeel_button.config(state=DISABLED)
        elif self.wind_true.get() and self.press_true.get():
            self.hum_button.config(state=DISABLED)
            self.temp_button.config(state=DISABLED)
            self.tempfeel_button.config(state=DISABLED)
        elif self.wind_true.get() and self.temp_true.get():
            self.hum_button.config(state=DISABLED)
            self.press_button.config(state=DISABLED)
        elif self.humidity_true.get() and self.temp_true.get():
            self.wind_button.config(state=DISABLED)
            self.press_button.config(state=DISABLED)
        elif self.press_true.get() and self.temp_true.get():
            self.hum_button.config(state=DISABLED)
            self.wind_button.config(state=DISABLED)
        elif self.wind_true.get() and self.temp_feel_true.get():
            self.hum_button.config(state=DISABLED)
            self.press_button.config(state=DISABLED)
        elif self.humidity_true.get() and self.temp_feel_true.get():
            self.wind_button.config(state=DISABLED)
            self.press_button.config(state=DISABLED)
        elif self.press_true.get() and self.temp_feel_true.get():
            self.hum_button.config(state=DISABLED)
            self.wind_button.config(state=DISABLED)
        else :
            self.hum_button.config(state=NORMAL)
            self.temp_button.config(state=NORMAL)
            self.tempfeel_button.config(state=NORMAL)
            self.press_button.config(state=NORMAL)
            self.wind_button.config(state=NORMAL)

    def check_cond_buttons(self):
        self.frame_checkbox = Frame(self.main, bg=self.gui_background)
        self.frame_checkbox.grid(row=9,column=3,sticky='w')
        self.temp_true=IntVar()
        self.temp_button=Checkbutton(self.frame_checkbox, text="Temperature", variable=self.temp_true, command=self.cb_check,bg=self.gui_background)
        self.temp_button.grid(row=8,column=2,sticky='w')
        self.temp_feel_true=IntVar()
        self.tempfeel_button=Checkbutton(self.frame_checkbox, text="Feel temperature", variable=self.temp_feel_true, command=self.cb_check, bg=self.gui_background)
        self.tempfeel_button.grid(row=8,column=3,sticky='w')
        self.press_true=IntVar()
        self.press_button=Checkbutton(self.frame_checkbox, text="Pressure", variable=self.press_true, command=self.cb_check, bg=self.gui_background)
        self.press_button.grid(row=8,column=4,sticky='w')
        self.humidity_true=IntVar()
        self.hum_button=Checkbutton(self.frame_checkbox, text="Humidity", variable=self.humidity_true, command=self.cb_check, bg=self.gui_background)
        self.hum_button.grid(row=9,column=3,sticky='w')
        self.wind_true=IntVar()
        self.wind_button=Checkbutton(self.frame_checkbox, text="Wind speed", variable=self.wind_true, command=self.cb_check, bg=self.gui_background)
        self.wind_button.grid(row=9,column=4,sticky='w')
        self.weather_desc=IntVar()
        self.wea_button=Checkbutton(self.frame_checkbox, text="Weather description", variable=self.weather_desc, command=self.cb_check, bg=self.gui_background)
        self.wea_button.grid(row=9,column=2,sticky='w')

    def weather_gui(self):
        self.current_weather()


        chloc_btn = Button(self.frame_displayboxex, text="Display forecast", command=self.five_d_weather)
        chloc_btn.grid(row=3,column=3,padx=2)
        self.check_cond_buttons()
        self.main.mainloop()


    def five_d_weather(self):
        color_arr=['darkblue','green','darkviolet','darkred','black','darkturquoise','slategray','olive','orangered']
        self.forecast_five_out=Weather(weather_type='forecast',city_name=self.city_name).Forecast_five_d()
        temp_arr=[round(i-273.15,2) for i in self.forecast_five_out.current_temperature]
        feel_temp_arr=[round(i-273.15,2) for i in self.forecast_five_out.feel_temperature]
        press_arr=[self.forecast_five_out.current_pressure][0]
        humidity_arr=[self.forecast_five_out.current_humidiy][0]
        wind_arr=[self.forecast_five_out.wind][0]
        #print(wind_arr)
        weather_desc_arr=[self.forecast_five_out.weather_description][0]

        time_arr=[int(i.split(" ")[2]) for i in self.forecast_five_out.calc_time]
        time_ref=[int(i.split(" ")[1]) for i in self.forecast_five_out.calc_time]
        diff_days=time_ref[0]

        iter=max(time_ref)
        for i in range(len(time_ref)):
            if time_ref[i]<time_ref[0]:
                if iter!=max(time_ref)+time_ref[i]:
                    iter+=1
                time_arr[i]=time_arr[i]+(24*(iter-time_ref[0]))
            else:
                time_arr[i]=time_arr[i]+(24*(time_ref[i]-time_ref[0]))

        b_ax = plt.gca()#Finish size and font of labels together with multiple y-axis label system
        n_of_lines=0
        ylabel_str=[]
        label_color=[]
        ylabel_strA=[]
        label_colorA=[]
        Display=False
        if self.temp_true.get()==1:
            Display=True
            if n_of_lines>=2:
                ax2=b_ax.twinx()
                ax2.plot(time_arr,temp_arr,'{}'.format(color_arr[n_of_lines]))
                ylabel_strA.append(u'Temperature [\u00b0C]')
                label_colorA.append(color_arr[n_of_lines])
            else:
                b_ax.plot(time_arr,temp_arr,'{}'.format(color_arr[n_of_lines]))
                ylabel_str.append(u'Temperature [\u00b0C]')
                label_color.append(color_arr[n_of_lines])
            #ax.yaxis.label.set_color('{}'.format(color_arr[n_of_lines]))
            n_of_lines+=1
        if self.temp_feel_true.get()==1:
            Display=True
            if n_of_lines>=2:
                ax2=b_ax.twinx()
                ax2.plot(time_arr,feel_temp_arr,'{}'.format(color_arr[n_of_lines]))
                ylabel_strA.append(u'Perceived temperature [\u00b0C]')
                label_colorA.append(color_arr[n_of_lines])
            else:
                b_ax.plot(time_arr,feel_temp_arr,'{}'.format(color_arr[n_of_lines]))
                ylabel_str.append(u'Perceived temperature [\u00b0C]')
                label_color.append(color_arr[n_of_lines])

            n_of_lines+=1
        if self.press_true.get()==1:
            Display=True
            if n_of_lines>=2 or self.temp_feel_true.get()==1 or self.temp_true.get()==1:
                ax2=b_ax.twinx()
                ax2.plot(time_arr,press_arr,'{}'.format(color_arr[n_of_lines]))
                ylabel_strA.append(u'Pressure [hPa]')
                label_colorA.append(color_arr[n_of_lines])
            else:
                b_ax.plot(time_arr,press_arr,'{}'.format(color_arr[n_of_lines]))
                ylabel_str.append(u'Pressure [hPa]')
                label_color.append(color_arr[n_of_lines])
                # ylabel_str.append(u'Pressure [hPa]')
                # label_color.append(color_arr[n_of_lines])
            n_of_lines+=1
        if self.humidity_true.get()==1:
            Display=True
            if n_of_lines>=2 or self.temp_feel_true.get()==1 or self.temp_true.get()==1 or self.press_true.get()==1 or self.wind_true.get()==1:
                ax2=b_ax.twinx()
                ax2.plot(time_arr,humidity_arr,'{}'.format(color_arr[n_of_lines]))
                ylabel_strA.append(u'Humidity [%]')
                label_colorA.append(color_arr[n_of_lines])
            else:
                b_ax.plot(time_arr,humidity_arr,'{}'.format(color_arr[n_of_lines]))
                ylabel_str.append(u'Humidity [%]')
                label_color.append(color_arr[n_of_lines])
            n_of_lines+=1
        if self.wind_true.get()==1:
            Display=True
            if n_of_lines>=2 or self.temp_feel_true.get()==1 or self.temp_true.get()==1 or self.press_true.get()==1:
                ax2=b_ax.twinx()
                ax2.plot(time_arr,wind_arr,'{}'.format(color_arr[n_of_lines]))
                ylabel_strA.append(u'Wind speed [ms$^{-1}$]')
                label_colorA.append(color_arr[n_of_lines])
            else:
                b_ax.plot(time_arr,wind_arr,'{}'.format(color_arr[n_of_lines]))
                ylabel_str.append(u'Wind speed [ms$^{-1}$]')
                label_color.append(color_arr[n_of_lines])

            n_of_lines+=1
        if self.weather_desc.get()==1:
            window = Toplevel(self.main)
            iter=0
            for i in range(len(time_arr)):

                temp_month=strptime(self.forecast_five_out.calc_time[i].split(' ')[0],'%b').tm_mon

                time_list = Label(window,text="{}.{} {}h: ".format(self.forecast_five_out.calc_time[i].split(' ')[1],temp_month,self.forecast_five_out.calc_time[i].split(' ')[2]))
                weather_list = Label(window,text="{}".format(weather_desc_arr[i]))

                time_list.grid(sticky='W',row=iter,column=0)
                weather_list.grid(sticky='W',row=iter,column=1)
                iter+=1
        if Display==True:
            i=0
            midnight_values=[]
            while 24*(i+1)<max(time_arr):
                midnight_values.append(24*(i+1))
                b_ax.axvline(x=24*(i+1))
                i+=1
            b_ax.set_xticks(midnight_values)

            date_arr=[]
            for i in self.forecast_five_out.calc_time:
                temp_value=i.split(' ')
                date_arr.append([strptime(temp_value[0],'%b').tm_mon,int(temp_value[1])])
            #date_arr=np.array(date_arr)
            mo_label=[]
            date_mem=0
            for i in range(len(date_arr)):
                if date_mem==date_arr[i][1]:
                    continue
                else:
                    mo_label.append(str(date_arr[i][1]+1)+'.'+str(date_arr[i][0]))
                    date_mem=date_arr[i][1]

            b_ax.xaxis.set_minor_locator(AutoMinorLocator(4))
            plt.setp(b_ax.get_xticklabels(minor=True), visible=True)
            # b_ax.set_xticklabels(mo_label)
            b_ax.set_xlabel('Time [Hours]',size=15,weight='bold')

            if len(plt.gcf().axes) == 2:
                multicolor_ylabel_double_ax(b_ax,ax2,(ylabel_str),(label_color),(ylabel_strA),(label_colorA),axis='y',size=15,weight='bold')
            else:
                multicolor_ylabel(b_ax,(ylabel_str),(label_color),axis='y',size=15,weight='bold')
            # if n_of_lines>2 or (self.temp_feel_true.get()==1 and self.temp_true.get()==1):
            #     multicolor_ylabel(b_ax,(ylabel_str),(label_color),axis='y',size=15,weight='bold')
            # elif n_of_lines>2 or self.temp_feel_true.get()==1 or self.temp_true.get()==1:
            #     multicolor_ylabel_double_ax(b_ax,ax2,(ylabel_str),(label_color),(ylabel_strA),(label_colorA),axis='y',size=15,weight='bold')
            # else:
            #     multicolor_ylabel(b_ax,(ylabel_str),(label_color),axis='y',size=15,weight='bold')

            plt.grid()
            mng = plt.get_current_fig_manager()
            # mng.resize(*mng.window.maxsize())
            # mng.window.state('zoomed')
            b_ax.tick_params(axis='x',which='both', width=4)
            b_ax.tick_params(axis='x',which='major', length=10, color='b')
            b_ax.tick_params(axis='x',which='minor', length=8)
            plt.title("You are currently located at the begging of the graph",fontsize=15)
            plt.show()
        else:
            pass
    def current_weather(self):
        self.text_bg="light green"
        self.gui_background="light green"
        self.vert_dist=5
        last_weather_update = Label(self.main,text="NaN")
        loc_name = Label(self.main,text="NaN")
        curr_temp=Label(self.main,text="NaN")
        ext_temp=Label(self.main,text="NaN")
        curr_press = Label(self.main,text="NaN")
        curr_hum =Label(self.main,text="NaN")
        weather_des = Label(self.main,text="NaN")
        sunrise = Label(self.main,text="NaN")
        sunset = Label(self.main,text="NaN")

        last_weather_update.grid(sticky="W",row=1,column=0,columnspan =3)
        loc_name.grid(sticky="W",row=2,column=0,columnspan =3)
        curr_temp.grid(sticky="W",row=3,column=0,columnspan =3)
        ext_temp.grid(sticky="W",row=4,column=0,columnspan =3)
        curr_press.grid(sticky="W",row=5,column=0,columnspan =3)
        curr_hum.grid(sticky="W",row=6,column=0,columnspan =3)
        weather_des.grid(sticky="W",row=7,column=0)
        sunrise.grid(sticky="W",row=8,column=0,columnspan =3)
        sunset.grid(sticky="W",row=9,column=0,columnspan =3)

        self.last_weather_update=last_weather_update
        self.loc_name=loc_name
        self.curr_temp=curr_temp
        self.ext_temp=ext_temp
        self.curr_press=curr_press
        self.curr_hum=curr_hum
        self.weather_des=weather_des
        self.sunrise=sunrise
        self.sunset=sunset

        if not hasattr(self, 'city_name'):
            self.city_name='Brno'
        #print(self.city_name)
        self.weather_output=Weather(weather_type='weather',city_name=self.city_name).Current()

        self.main.configure(background=self.gui_background)
        self.last_weather_update.configure(text="Last weather update was at : {}".format(self.weather_output.calc_time), font=("Arial Bold", 16), bg=self.text_bg, pady=self.vert_dist)
        self.loc_name.configure(text="Location : {} ({})".format(self.weather_output.location,self.weather_output.country), font=("Arial Bold", 16), bg=self.text_bg, pady=self.vert_dist)
        self.curr_temp.configure(text=u"Temperature is : {}\u00b0C, Perceived temperature : {}\u00b0C".format(round(self.weather_output.current_temperature- 273.15,2),round(self.weather_output.feel_temperature- 273.15,2)), font=("Arial Bold", 16), bg=self.text_bg, pady=self.vert_dist)
        self.ext_temp.configure(text="Temperature range is : {}-{}\u00b0C".format(round(self.weather_output.min_temperature- 273.15,2),round(self.weather_output.max_temperature- 273.15,2)), font=("Arial Bold", 16), bg=self.text_bg, pady=self.vert_dist)
        self.curr_press.configure(text="Pressure is : {}".format(self.weather_output.current_pressure)+"hPa", font=("Arial Bold", 16), bg=self.text_bg, pady=self.vert_dist)
        self.curr_hum.configure(text="Humidity is : {}".format(self.weather_output.current_humidiy)+"%", font=("Arial Bold", 16), bg=self.text_bg, pady=self.vert_dist)
        self.weather_des.configure(text="Description : {}".format(self.weather_output.weather_description), font=("Arial Bold", 16), bg=self.text_bg, pady=self.vert_dist)
        self.sunrise.configure(text="Sunrise is today at : {}".format(self.weather_output.sunrise), font=("Arial Bold", 16), bg=self.text_bg, pady=self.vert_dist)
        self.sunset.configure(text="Sunset is today at : {}".format(self.weather_output.sunset), font=("Arial Bold", 16), bg=self.text_bg, pady=self.vert_dist)

        img_sky=ImageTk.PhotoImage(self.weather_output.icon)
        img_ref=Label(self.main,image=img_sky,background=self.gui_background,height=20)
        img_ref.image = img_sky
        img_ref.grid(row = 7, column = 1,sticky='w')

        chloc_input = Entry(self.frame_displayboxex,width=10)
        chloc_btn = Button(self.frame_displayboxex, text="Change location", command=self.ch_loc_press)
        chloc_btn.grid(row=1,column=3,padx=2)
        chloc_input.grid(row=1,column=2,sticky='e')


        self.chloc_input=chloc_input
        self.auto_weather_update()
        self.clock()


    def auto_weather_update(self):
        if not hasattr(self, 'city_name'):
            self.city_name='Brno'
        self.curr_weather_rewrite()
        self.main.after(1000, self.auto_weather_update)

    def curr_weather_rewrite(self):
        self.weather_output=Weather(weather_type='weather',city_name=self.city_name).Current()

        self.main.configure(background=self.gui_background)
        self.last_weather_update.configure(text="Last weather update was at : {}".format(self.weather_output.calc_time), font=("Arial Bold", 16), bg=self.text_bg, pady=self.vert_dist)
        self.loc_name.configure(text="Location : {} ({})".format(self.weather_output.location,self.weather_output.country), font=("Arial Bold", 16), bg=self.text_bg, pady=self.vert_dist)
        self.curr_temp.configure(text=u"Temperature is : {}\u00b0C, Perceived temperature : {}\u00b0C".format(round(self.weather_output.current_temperature- 273.15,2),round(self.weather_output.feel_temperature- 273.15,2)), font=("Arial Bold", 16), bg=self.text_bg, pady=self.vert_dist)
        self.ext_temp.configure(text="Temperature range is : {}-{}\u00b0C".format(round(self.weather_output.min_temperature- 273.15,2),round(self.weather_output.max_temperature- 273.15,2)), font=("Arial Bold", 16), bg=self.text_bg, pady=self.vert_dist)
        self.curr_press.configure(text="Pressure is : {}".format(self.weather_output.current_pressure)+"hPa", font=("Arial Bold", 16), bg=self.text_bg, pady=self.vert_dist)
        self.curr_hum.configure(text="Humidity is : {}".format(self.weather_output.current_humidiy)+"%", font=("Arial Bold", 16), bg=self.text_bg, pady=self.vert_dist)
        self.weather_des.configure(text="Description : {}".format(self.weather_output.weather_description), font=("Arial Bold", 16), bg=self.text_bg, pady=self.vert_dist)
        self.sunrise.configure(text="Sunrise is today at : {}".format(self.weather_output.sunrise), font=("Arial Bold", 16), bg=self.text_bg, pady=self.vert_dist)
        self.sunset.configure(text="Sunset is today at : {}".format(self.weather_output.sunset), font=("Arial Bold", 16), bg=self.text_bg, pady=self.vert_dist)

        img_sky=ImageTk.PhotoImage(self.weather_output.icon)
        img_ref=Label(self.main,image=img_sky,background=self.gui_background,height=20)
        img_ref.image = img_sky
        img_ref.grid(row = 7, column = 1,sticky='w')

    def ch_loc_press(self):
        self.city_name=self.chloc_input.get()
        self.curr_weather_rewrite()

    def clock(self):
        time = datetime.datetime.now().strftime("Time: %H:%M:%S")
        self.time.config(text=time, font=("Arial Bold", 25), bg="green")
        #lab['text'] = time
        self.main.after(1000, self.clock) # run itself again after 1000 ms

interface()
