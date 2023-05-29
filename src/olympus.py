from elevation_getter import ElevationGetter
from coord_field import CoordField
from graph import Graph 
from franklin_and_ray import FranklinAndRay
from visualizer import Visualizer
from analytics import Analytics
from helpers import calcArea,reconcileCoords, get_fake_elevations
#class to run the view shed for a single location
class Olympus:
    def __init__(self,x,y,h,r,s):
        self.x = x
        self.y = y
        self.h = h 
        self.r = r 
        self.s = s
        self.cf = CoordField(x,y,r,s)
        self.cf.fill_field()
        #print(len(self.cf.xList))
     
        # self.ele = ElevationGetter(self.cf.longitude_list,self.cf.latitude_list)
        # self.elevations = self.ele.getElevation()
        self.elevations = get_fake_elevations(int((r/s)*2-1))
       
        self.graph = Graph(int(self.r/self.s),self.elevations)
        self.fam = FranklinAndRay(self.graph,self.h)
        self.fam.run_franklin_and_ray()
        self.fam.calc_views()

    def getAPIReturnList(self):
        APIReturn = []
        APIReturn2 = reconcileCoords(self.graph.grid_list,self.cf.longitude_list,self.cf.latitude_list,self.fam.vs)
        return APIReturn2
            
    def visualize(self,areas,heights):
        xS = self.graph.x_list()
        yS = self.graph.y_list()
        zS = self.graph.z_list()
        xS2 = self.fam.x_list()
        yS2 = self.fam.y_list()
        zS2 = self.fam.z_list()

        v = Visualizer(xS,yS,zS,xS2,yS2,zS2,areas,heights)
        v.visualize()

    def multH(self, low,high):
        x = high - low
        areas = []
        for i in range(x):
            newH = low + i
            fAMx = FranklinAndRay(self.graph,newH)
            fAMx.run_franklin_and_ray()
            fAMx.calc_views()
            anax = Analytics(self.r,newH,self.s,fAMx)
            anax.calcAreas()
            areas.append(anax.totArea)
        return areas
