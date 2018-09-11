from tkinter import *
import requests
import psutil
import platform
import cpuinfo

class System_IP_Weather:

    def __init__(self, root):
        root.title("System_Info,IP_Info,Weather_info")
        root.geometry("600x750")
        root.resizable(width=False, height=False)

        root.configure(background="#3575a3")
        # System Information
        winVersion = platform.platform()
        sysType = platform.architecture()
        cpuModel = cpuinfo.get_cpu_info()['brand']
        cpuCores = psutil.cpu_count()

        self.emptyLine = Label(root,text = "\n\n", bg ="#3575a3").pack()

        self.buttonSysInfo = Label(root, text="System Information", font='Helvetica 18 bold', bg="black",fg="white")
        self.buttonSysInfo.pack(fill=X, padx=50, pady=0)

        self.buttonWinVersion = Label(root, text="Windows version: {}".format(winVersion),
                                      font='Helvetica 14 bold', bg = "#00ccff")
        self.buttonWinVersion.pack(fill=X, padx=50, pady=0)

        self.buttonSysType = Label(root, text="System Type: {}".format(sysType[0]),font='Helvetica 14 bold', bg ="#00ccff")
        self.buttonSysType.pack(fill=X, padx=50, pady=0)
        self.buttonCpuModel = Label(root, text="CPU: {}".format(cpuModel),font='Helvetica 14 bold', bg ="#00ccff")
        self.buttonCpuModel.pack(fill=X, padx=50, pady=0)
        self.buttonCpuCores = Label(root, text="Number of Cores: {}".format(cpuCores),font='Helvetica 14 bold', bg ="#00ccff")
        self.buttonCpuCores.pack(fill=X, padx=50, pady=0)
        self.emptyLine = Label(root,text = "\n\n", bg ="#3575a3").pack()


        # Service Provider Information
        url = 'https://ipinfo.io'
        res = requests.get(url)
        data = res.json()

        ip = data['ip']
        city = data['city']
        state = data['region']
        zipCode = data['postal']
        provider = data['org']
        location = data['loc'].split(',')
        latitude = location[0]
        longitude = location[1]

        self.buttonSysInfo = Label(root, text="Internet Service Provider Information", font='Helvetica 18 bold', bg="black", fg="white")
        self.buttonSysInfo.pack(fill=X, padx=50, pady=0)

        self.buttonProvider = Label(root, text="Provider: {}".format(provider[8:]), font='Helvetica 14 bold',
                                    bg="#00cc66")
        self.buttonProvider.pack(fill=X, padx=50, pady=0)

        self.buttonIP = Label(root, text="IP Address: {}".format(ip),font='Helvetica 14 bold', bg ="#00cc66")
        self.buttonIP.pack(fill=X, padx=50, pady=0)

        self.buttonCity = Label(root, text="City: {}".format(city),font='Helvetica 14 bold', bg ="#00cc66")
        self.buttonCity.pack(fill=X, padx=50, pady=0)

        self.buttonState = Label(root, text="State: {}".format(state),font='Helvetica 14 bold', bg ="#00cc66")
        self.buttonState.pack(fill=X, padx=50, pady=0)

        self.buttonZip = Label(root, text="Zip Code: {}".format(zipCode),font='Helvetica 14 bold', bg ="#00cc66")
        self.buttonZip.pack(fill=X, padx=50, pady=0)



        self.emptyLine = Label(root,text = "\n\n", bg ="#3575a3").pack()


        # Weather Information
        urlWeather = 'http://api.openweathermap.org/data/2.5/weather?lat={}&lon={}&appid=f5630c108657fd0b0f67d00fa6448d34&' \
                     'units=imperial'.format(latitude, longitude)
        # Make the connection with the given url
        resWeather = requests.get(urlWeather)
        # Store the connection data unit a variable
        dataWeather = resWeather.json()

        # Use map key format to access a specific value
        temp = dataWeather['main']['temp']
        humidity = dataWeather['main']['humidity']
        pressure = dataWeather['main']['pressure']
        windSpeed = dataWeather['wind']['speed']
        description = dataWeather['weather'][0]['description']

        self.buttonSysInfo = Label(root, text="Weather Information", font='Helvetica 18 bold',
                                   bg="black", fg="white")
        self.buttonSysInfo.pack(fill=X, padx=50, pady=0)
        self.buttonTitle = Label(root, text="Weather at: {}".format(city),font='Helvetica 14 bold', bg ="#fe9126")
        self.buttonTitle.pack(fill=X, padx=50, pady=0)
        self.buttonTemp = Label(root, text="Temperature: {} °F".format(temp),font='Helvetica 14 bold', bg ="#fe9126")
        self.buttonTemp.pack(fill=X, padx=50, pady=0)
        self.buttonHumidity= Label(root, text="Humidity: {} %".format(humidity),font='Helvetica 14 bold', bg ="#fe9126")
        self.buttonHumidity.pack(fill=X, padx=50, pady=0)
        self.buttonPressure = Label(root, text="Pressure: {} hPa".format(pressure),font='Helvetica 14 bold', bg ="#fe9126")
        self.buttonPressure.pack(fill=X, padx=50, pady=0)
        self.buttonWindSpeed = Label(root, text="Wind Speed: {} mph".format(windSpeed),font='Helvetica 14 bold', bg ="#fe9126")
        self.buttonWindSpeed.pack(fill=X, padx=50, pady=0)
        self.buttonDescription = Label(root, text="Description: {}".format(description),font='Helvetica 14 bold', bg ="#fe9126")
        self.buttonDescription.pack(fill=X, padx=50, pady=0)

if __name__ == "__main__":
    root = Tk()
    information = System_IP_Weather(root)
    root.mainloop()