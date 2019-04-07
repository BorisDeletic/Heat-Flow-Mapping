from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import data_analysis
import pandas as pd
import re
import matplotlib.animation as animation


class LivingRoom():
    def __init__(self):
        data = data_analysis.DataAnalysis("H_data.csv")
        self.df = data.df
        self.layout_room("room_layout.csv", 'sensor_layout.csv')
        self.plot2D()

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

        res = 1
        padding = 50
        
        X = np.arange(boundsX[0] - padding, boundsX[1] + padding, res)
        Y = np.arange(boundsY[0] - padding, boundsY[1] + padding, res)
        X, Y = np.meshgrid(X, Y)

        print(X[2], Y[2])


    def plot3D(self):
        self.format_3D_data()

        fig = plt.figure()
        ax = fig.gca(projection='3d')

        # Make data.
        X = np.arange(-5, 5, 0.25)
        Y = np.arange(-5, 5, 0.25)

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


    def plot2D(self):
        self.temps = np.vstack(self.df.values[:, 1:]).astype(np.float)


        print(self.temps)
        fig, ax = plt.subplots()

        r = np.transpose([np.linspace(1, 0.6,10)])
        g = np.transpose([np.zeros(10)])
        b = np.transpose([np.zeros(10)])
        colors = np.concatenate((r,g,b), axis=1)
        colormap = ListedColormap(colors)

        norm = plt.Normalize(self.temps.min(), self.temps.max())
        self.sc = ax.scatter(self.sen_pos[0], self.sen_pos[1], c=self.temps[0], s=500, cmap=cm.coolwarm, norm = norm)

     #   ax.scatter(self.sen_pos[0], self.sen_pos[1], c=temps, cmap = colormap, s = 400)
        ax.plot(self.verts[0], self.verts[1], color = 'black')        
        
        ax.set_facecolor((0.8,0.8,0.8))
        plt.axis('scaled')

        dt = 50
        ani = animation.FuncAnimation(fig, self.animate, frames=range(len(self.temps)), interval = dt)
        plt.show()

    def animate(self, i):
        self.sc.set_array(self.temps[i])
        
        


LivingRoom()


