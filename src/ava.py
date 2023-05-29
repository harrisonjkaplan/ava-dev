from elevation_getter import ElevationGetter
from coord_field import CoordField
from graph import Graph 
from franklin_and_ray import FranklinAndRay
from visualizer import Visualizer
from helpers import reconcileCoords, get_fake_elevations, difference_of_views
#class to run the view shed for a single location
class Ava:
    def __init__(self,x,y,r,s,min_height=0,max_height=0):
        self.x = x
        self.y = y
        self.min_height = min_height 
        self.max_height = max_height
        self.r = r 
        self.s = s
        self.cf = CoordField(x,y,r,s)
        self.cf.fill_field()
     
        # self.ele = ElevationGetter(self.cf.longitude_list,self.cf.latitude_list)
        # self.elevations = self.ele.getElevation()
        self.elevations = get_fake_elevations(int((r/s)*2-1))
        self.graph = Graph(int(self.r/self.s),self.elevations)


        self.fams = []

    def getAPIReturnList(self):
        APIReturn = []
        # APIReturn2 = reconcileCoords(self.graph.grid_list,self.cf.longitude_list,self.cf.latitude_list,self.fam.vs)
        # return APIReturn2
    
    def calc_viewsheds(self):
        for height in range(self.min_height,self.max_height):
            fam = FranklinAndRay(self.graph,height,self.s)
            fam.run_franklin_and_ray()
            fam.calc_views()
            fam.set_area_of_views()
            self.fams.append(fam)
            if height != 0:
                fam.new_coords = difference_of_views(self.fams[height-self.min_height-1].vs,self.fams[height-self.min_height].vs)

    def get_areas(self):
        areas = []
        for fam in self.fams:
            areas.append(fam.get_area_of_views())
        return areas

            
    def visualize(self,areas,heights):
        xS = self.graph.x_list()
        yS = self.graph.y_list()
        zS = self.graph.z_list()
        xS2 = self.fams[0].x_list()
        yS2 = self.fams[0].y_list()
        zS2 = self.fams[0].z_list()

        v = Visualizer(xS,yS,zS,xS2,yS2,zS2,areas,heights)
        v.visualize()
