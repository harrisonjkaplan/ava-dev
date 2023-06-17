import math 
from .helpers import get_perimeter, slope,bres,contains_coord,order_vs,dfs,difference_of_views
from bresenham import bresenham
from .coordinates import Coord, Graph, View
import numpy as np
class FranklinAndRay:
    def __init__(self,graph,h,s): 
        self.graph = graph #graph of easier coordinates from Graph.py
        self.h = h
        self.s = s
        self.vs = []
        self.perimeter = []#perimeter
        self.views = []
        self.ordered_vs = []
        self.new_coords = []
        self.total_vs_area = 0


#implementation of franklinandray's algorithm for calculating view shed
    def run_franklin_and_ray(self):
        observer_x_val = self.graph.grid[self.graph.num_steps-1][self.graph.num_steps-1].x
        observer_y_val = self.graph.grid[self.graph.num_steps-1][self.graph.num_steps-1].y
        observer_ele_val = self.graph.grid[self.graph.num_steps-1][self.graph.num_steps-1].z
        obs = Coord(observer_x_val,observer_y_val,observer_ele_val)
        self.perimeter = get_perimeter(self.graph) 

        for i in range(len(self.perimeter)):
            u=-1000000
            sight_line = bres(self.graph.grid,obs,self.perimeter[i],self.graph.num_steps)
              
            for j in range(len(sight_line)-1):
                mi = slope(obs,sight_line[j+1],self.h)
                
                if(mi>=u):
                    u = mi
        
                    if(contains_coord(sight_line[j+1],self.vs) == False):
                        self.vs.append(sight_line[j+1])
                        print(self.vs[-1].coordinates_to_string())
                        grid_y = -sight_line[j+1].y-1+self.graph.num_steps
                        grid_x = sight_line[j+1].x-1+self.graph.num_steps
                        self.graph.grid[grid_y][grid_x].view = 0


    def get_vs_coords(self):
        vs_coords = []
        for i in range(len(self.graph.grid)):
            for j in range(len(self.graph.grid[i])):
                if self.graph.grid[i][j].view == 0:
                    vs_coords.append(self.graph.grid[i][j])

        return vs_coords
            

    def calc_views(self):
        vs_coords = self.get_vs_coords()
        self.ordered_vs = order_vs(vs_coords,self.graph.num_steps)
        dfs_result = dfs(self.ordered_vs,self.ordered_vs[0])
        first_view = View()
        first_view.add_coords(dfs_result)
        self.views.append(first_view)
        coords_left = difference_of_views(dfs_result,self.ordered_vs)

        while(0<len(coords_left)):
            dfsi = dfs(coords_left,coords_left[0])
            new_view = View()
            new_view.add_coords(dfsi)
            self.views.append(new_view)
            coords_left = difference_of_views(dfsi,coords_left)

    def set_area_of_views(self):
        for view in self.views:
            view_area = len(view.coords)*self.s**2
            view.set_area(view_area) 
            self.total_vs_area = self.total_vs_area + view_area

    def get_area_of_views(self):
        areas = [view.area for view in self.views]
        return areas
    
    def to_dict(self):
        dict_obj = {}
        print(self.vs[0].coordinates_to_string())
        visible_points = [coord.coordinates_to_string() for coord in self.vs]

        dict_obj['visible_points'] = visible_points
        dict_obj['total_visible_area'] = self.total_vs_area
        dict_obj['newly_visible_points'] = [coord.coordinates_to_string() for coord in self.new_coords]
        views = []
        for view in self.views:
            view_details = {}
            view_details['visible_points'] = [coord.coordinates_to_string() for coord in view.coords]
            view_details['area'] = view.area
            views.append(view_details)
        dict_obj['view'] = views

        return dict_obj


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
