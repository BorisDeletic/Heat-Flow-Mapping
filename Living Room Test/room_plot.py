from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import data_analysis
import pandas as pd
import re


class LivingRoom():
    def __init__(self):
        data = data_analysis.DataAnalysis("H_data.csv")
        self.df = data.df
        self.layout_room("room_layout.csv", 'sensor_layout.csv')
        self.plot()

    def layout_room(self, room_file, sensor_file):
        with open(room_file) as f:
            direct = f.readline().split(',')

        dist = []
        bearings = []
        for inst in direct:
            dist.append(int(re.split('(\d+)', inst)[1])) ## second element for some resn
            bearings.append(re.split('(\d+)', inst)[2])

        verts = np.array([[0], [0]])
        sensors = np.array([[0], [0]])
        dist.pop(0)
        bearings.pop(0) # remove initial Up instruction

        self.verts = self.add_verticies(verts, dist, bearings)

        self.sen_pos = np.genfromtxt(sensor_file, delimiter = ',').T
        
##        print(verts.T)
##        fig, ax = plt.subplots()
##        ax.plot(verts[0], verts[1])
##        ax.scatter(sen_data[0], sen_data[1], color='red')
##        plt.axis('scaled')
##        plt.show()

    def add_verticies(self, verts, dist, bearings):
        for i in range(len(bearings)):
            if bearings[i] == 'N':
                newY = verts[1][-1] + dist[i]
                verts = np.concatenate((verts, [[verts[0][-1]], [newY]]), axis = 1)
                
            if bearings[i] == 'S':
                newY = verts[1][-1] - dist[i]
                verts = np.concatenate((verts, [[verts[0][-1]], [newY]]), axis = 1)
                
            if bearings[i] == 'E':
                newX = verts[0][-1] + dist[i]
                verts = np.concatenate((verts, [[newX], [verts[1][-1]]]), axis = 1)
                
            if bearings[i] == 'W':
                newX = verts[0][-1] - dist[i]
                verts = np.concatenate((verts, [[newX], [verts[1][-1]]]), axis = 1)

        return verts


    def format_3D_data(self):
        boundsX = [self.verts[0].min(), self.verts[0].max()]
        boundsY = [self.verts[1].min(), self.verts[1].max()]

        res = 50
        
        X = np.arange(boundsX[0] - res, boundsX[1] + res, res)
        Y = np.arange(boundsY[0] - res, boundsY[1] + res, res)
        
        

    def plot(self):
        print(self.df.loc[0][3])
        
        fig = plt.figure()
        ax = fig.gca(projection='3d')

        # Make data.
        X = np.arange(-5, 5, 0.25)
        Y = np.arange(-5, 5, 0.25)

        print(X,Y)
        X, Y = np.meshgrid(X, Y)
        Z = np.zeros(X.shape)
        Z[6][5] = 1


        # Plot the surface.
        surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                               linewidth=0, antialiased=False)

        # Customize the z axis.
        ax.set_zlim(-1.01, 1.01)
        ax.zaxis.set_major_locator(LinearLocator(10))
        ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

        # Add a color bar which maps values to colors.
        fig.colorbar(surf, shrink=0.5, aspect=5)

        plt.show()


LivingRoom()


