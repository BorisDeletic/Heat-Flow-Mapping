import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates 


df = pd.read_csv("data.csv")


df["Time"] = pd.to_datetime(df["Time"], format = "%Y-%m-%d %H:%M:%S")

df["Time"] = matplotlib.dates.date2num(df["Time"])



#plt.plot_date(df["Time"], df["Temp0"])

fig, ax = plt.subplots()

#ax.plot(df["Time"], df[["Temp0", "Temp1", "Temp2", "Temp3"]])
ax.plot(df["Time"], df["Temp0"], label = "Sensor 1")
ax.plot(df["Time"], df["Temp1"], label = "Sensor 2")
ax.plot(df["Time"], df["Temp2"], label = "Sensor 3")
ax.plot(df["Time"], df["Temp3"], label = "Sensor 4")


plt.legend(loc='upper left')
ax.set_title("Temperature vs Time")
plt.ylabel("Degrees (\N{DEGREE SIGN}C)")
plt.show()



