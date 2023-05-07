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
        print((r/s)*2-1)
        self.elevations = get_fake_elevations(int((r/s)*2-1))
       
        self.gr1 = Graph(int(self.r/self.s),self.elevations)
        self.fAM = FranklinAndRay(self.gr1,self.h)
        self.fAM.runFranklinAndRay()
        self.fAM.calcViews()


        #print(list1[0])
    def getAPIReturnList(self):
        APIReturn = []
        APIReturn2 = reconcileCoords(self.gr1.grid_list,self.cf.longitude_list,self.cf.latitude_list,self.fAM.vs)
        return APIReturn2
            
    def visualize(self,areas,heights):

        xS = self.gr1.x_list()
        yS = self.gr1.y_list()
        zS = self.gr1.z_list()
        xS2 = self.fAM.x_list()

        yS2 = self.fAM.y_list()
        zS2 = self.fAM.z_list()
   

        v = Visualizer(xS,yS,zS,xS2,yS2,zS2,areas,heights)
        v.visualize()
    def multH(self, low,high):
        x = high - low
        areas = []
        for i in range(x):
            newH = low + i
            fAMx = FranklinAndRay(self.gr1,newH)
            fAMx.runFranklinAndRay()
            fAMx.calcViews()
            anax = Analytics(self.r,newH,self.s,fAMx)
            anax.calcAreas()
            areas.append(anax.totArea)
        return areas
