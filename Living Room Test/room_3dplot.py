from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np

fpdft = 'roomData'

class plotRoom:
    def __init__(self, scene, datafp = fpdft):
        self.datafp = datafp
        self.verts = np.zeros((0,3))
        self.edges = np.zeros((0,2))
        self.__loadDataFile()
        self.plot(scene)
    
    def __loadDataFile(self):
        with open(self.datafp + '/room_verts.csv', 'r') as vertsF:
            for row in vertsF:
                vert = row
                vert = vert.replace('\n',' ')
                vert = vert.split(',')
                self.verts = np.append(self.verts, [vert], axis = 0)
        
        self.verts = self.verts.astype(np.float64)
        
        with open(self.datafp + '/room_edges.csv', 'r') as edgesF:
            for row in edgesF:
                edge = row
                edge = edge.replace('\n',' ')
                edge = edge.split(',')
                self.edges = np.append(self.edges, [edge], axis = 0)
        
        self.edges = self.edges.astype(int)
        self.edges = self.edges - 1


    def plot(self, scene):
        
        ax = scene.add_subplot(111, projection='3d')
        
        x = self.verts[:,0]
        y = self.verts[:,1]
        z = self.verts[:,2]
        ax.scatter(x,y,z, c = 'b', marker = 'o')
        
        for row in self.edges:

            xe = np.array([x[row[0]],x[row[1]]])
            ye = np.array([y[row[0]],y[row[1]]])
            ze = np.array([z[row[0]],z[row[1]]])
            
            ax.plot(xe,ye,ze, c = 'b', marker = ' ')
        
        
        
        
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
        

scene = plt.figure()        
plotRoom(scene)
plt.show()