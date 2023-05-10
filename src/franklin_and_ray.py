import math 
from helpers import get_perimeter, slope,coordsEqual,containsCoord,bres,containsCoord2, adjacentPointCheck,orderVS,dfs,differenceofViews
from bresenham import bresenham
from coord import Coord
from view import View
from graph import Graph
import numpy as np
class FranklinAndRay:
    def __init__(self,graph,h): 
        self.graph = graph #graph of easier coordinates from Graph.py
        self.h = h
        self.lines = []
        self.vs = []
        self.perimeter = []#perimeter
        self.views = []
        self.vs2 = []


#implementation of franklinandray's algorithm for calculating view shed
    def runFranklinAndRay(self):
        observer_x_val = self.graph.grid[self.graph.num_steps-1][self.graph.num_steps-1].get_x()
        observer_y_val = self.graph.grid[self.graph.num_steps-1][self.graph.num_steps-1].get_y()
        observer_ele_val = self.graph.grid[self.graph.num_steps-1][self.graph.num_steps-1].get_z()
        obs = Coord(observer_x_val,observer_y_val,observer_ele_val)
        self.perimeter = get_perimeter(self.graph) 

        for i in range(len(self.perimeter)):
            u=-1000000
            line = bres(self.graph.grid,obs,self.perimeter[i],self.graph.num_steps)
            l1 = []
            for j in range(len(line)-1):
                mi = slope(obs,line[j+1],self.h)
                
                if(mi>=u):
                    u = mi
                    
                    if(containsCoord2(line[j+1],self.vs) == False):
                        self.vs.append(line[j+1])
                        l1.append(line[j+1])
            self.lines.append(l1)
            

    def calcViews(self):
        
        self.vs2 = orderVS(self.vs,self.graph.num_steps)
        dfs1 = dfs(self.vs2,self.vs2[0])
        v1 = View()
        v1.addCoord(dfs1)
        self.views.append(v1)
        i = 0
        coordsLeft = differenceofViews(dfs1,self.vs2)

        while(0<len(coordsLeft)):
            dfsi = dfs(coordsLeft,coordsLeft[0])
            vi = View()
            vi.addCoord(dfsi)
            self.views.append(vi)
            coordsLeft = differenceofViews(dfsi,coordsLeft)

    def printViews(self):
        for i in range(len(self.views)):
            #print("View: ",end="")
            #print(i)
            #self.views[i].getCoords()
            x = 0


    def x_list(self):
        xS = []
        for i in range(len(self.vs)):
             xS.append(self.vs[i].get_x())
        return xS
    
    def y_list(self):
        yS = []
        for i in range(len(self.vs)):
            yS.append(self.vs[i].get_y())
        return yS
    
    def z_list(self):
        zS = []
        for i in range(len(self.vs)):
            zS.append(self.vs[i].get_z())
        return zS
    
    def get_z_val(self,x,y):
        for coord in self.vs:
            if coord.x == x and coord.y == y:
                return coord.z
        return "coord does not exist"
