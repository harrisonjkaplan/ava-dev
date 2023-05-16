import math 
from helpers import get_perimeter, slope,coords_equal,containsCoord,bres,contains_coord, adjacentPointCheck,order_vs,dfs,differenceofViews, get_elevation
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
        self.ordered_vs = []


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
                    
                    if(contains_coord(line[j+1],self.vs) == False):
                        self.vs.append(line[j+1])
                        l1.append(line[j+1])
            self.lines.append(l1)
            

    def calc_views(self):
        self.ordered_vs = order_vs(self.vs,self.graph.num_steps)
        dfs_result = dfs(self.ordered_vs,self.ordered_vs[0])
        first_view = View()
        first_view.add_coords(dfs_result)
        self.views.append(first_view)
        coords_left = differenceofViews(dfs_result,self.ordered_vs)

        while(0<len(coords_left)):
            dfsi = dfs(coords_left,coords_left[0])
            new_view = View()
            new_view.add_coords(dfsi)
            self.views.append(new_view)
            coords_left = differenceofViews(dfsi,coords_left)

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
