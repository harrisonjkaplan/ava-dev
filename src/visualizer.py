
import numpy as np
import matplotlib.pyplot as plt 
from matplotlib import cm
from mpl_toolkits import mplot3d
import matplotlib.colors as colors
#Simple visualizer to show the coordinates and their respective elevations 
class Visualizer:

    def __init__(self,x,y,z,x2,y2,z2,areas,heights):
        self.x = x 
        self.y = y 
        self.z = z 
        self.x2 = x2
        self.y2 = y2 
        self.z2 = z2
        self.areas = areas
        self.heights = heights
    

    def visualize(self):
        X = np.array(self.x)
        Y = np.array(self.y)
        Z = np.array(self.z)
        X2 = np.array(self.x2)
        Y2 = np.array(self.y2)
        Z2 = np.array(self.z2)
        npAreas = np.array(self.areas)
        npHeights = np.array(self.heights)




        #fig = plt.figure()
        fig = plt.figure(figsize=plt.figaspect(2.))
        ax = fig.add_subplot(5, 1, 1)

        ax.plot(npHeights,npAreas)
        ax.grid(True)
        ax.set_ylabel('Height analysis')
        ax = plt.axes(projection = "3d")


        ax.plot_trisurf(X,Y,Z,color="blue")
        ax.scatter3D(X2, Y2, Z2, color="red")


        plt.show()
