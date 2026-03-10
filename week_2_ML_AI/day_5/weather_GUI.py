import matplotlib
import tkinter as tk
from datetime import datetime, timedelta
import pytz
from weather_for_gui import humidity_list, days
import matplotlib.pyplot as plt

root = tk.Tk()
myLabel = tk.Label(root, text ='Humidity Forecast')# creation du label comme une assignation
myLabel.pack()# place optionnelement notre label tout en haut au milieu
plt.title("Humidity Forecast")
plt.ylabel("Humidity (%)")
plt.xlabel('Days')


plt.bar(days, humidity_list)
plt.show()
root.mainloop()