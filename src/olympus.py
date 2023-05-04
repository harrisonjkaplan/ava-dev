from elevation_getter import ElevationGetter
from coord_field import CoordField
from graph import Graph 
from franklin_and_ray import FranklinAndRay
from visualizer import Visualizer
from analytics import Analytics
from helpers import zList,calcArea,yList,xList,reconcileCoords
#class to run the view shed for a single location
class Olympus:
    def __init__(self,x,y,h,r,s):
        self.x = x
        self.y = y
        self.h = h 
        self.r = r 
        self.s = s
        self.cf = CoordField(x,y,r,s)
        self.cf.fillField()
        #print(len(self.cf.xList))
     
        self.ele = ElevationGetter(self.cf.longitude_list,self.cf.latitude_list)
        self.elevations = self.ele.getElevation()
       
        self.gr1 = Graph(int(self.r/self.s),self.elevations,self.cf)
        self.fAM = FranklinAndRay(self.gr1,self.h)
        self.fAM.runFranklinAndRay()
        self.fAM.calcViews()


        #print(list1[0])
    def getAPIReturnList(self):
        APIReturn = []
        APIReturn2 = reconcileCoords(self.gr1.gList,self.cf.longitude_list,self.cf.latitude_list,self.fAM.vs)
        return APIReturn2
            
    def visualize(self,areas,heights):

        xS = self.gr1.xList()
        yS = self.gr1.yList()
        zS = self.gr1.zList()
        xS2 = xList(self.fAM.vs)

        yS2 = yList(self.fAM.vs)
        zS2 = zList(self.fAM.vs)
   

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
