import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates 


class Grapher():
    def __init__(self, data_file):
        data_file
        self.df = pd.read_csv(data_file)

      #  self.join_files("V_data.csv")

        new_columns = ["Time"]
        self.num_sens = len(self.df.columns)-1

        for i in range(self.num_sens):
            new_columns.append("Temp"+str(i))

        self.df.columns = new_columns

        self.df["Time"] = pd.to_datetime(self.df["Time"], format = "%Y-%m-%d %H:%M:%S")
        self.plot()


    def plot(self):
        fig, ax = plt.subplots()

        for i in range(self.num_sens):
            ax.plot(self.df["Time"], self.df["Temp" + str(i)], label = "Sensor " + str(i))

        plt.legend(loc='upper left')
        ax.set_title("Temperature vs Time")
        plt.ylabel("Degrees (\N{DEGREE SIGN}C)")
        plt.show()

    def join_files(self, file_tojoin):
        ## files must have the same shape. joins file_tojoin at the end
        df_tojoin = pd.read_csv(file_tojoin)

        self.df = self.df.append(df_tojoin)
        print(self.df)
            
        


Grapher("H_data.csv")


