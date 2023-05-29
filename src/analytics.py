from helpers import calcArea, sameofViews,difference_of_views
from view import View
#to do
    #degrees of range in each view
    #predictions 
class Analytics:
    def __init__(self,r,h,s,fAM):
        self.r = r 
        self.s = s
        self.h = h
        self.fAM = fAM 
        self.totArea = 0

        self.perim = []


    def calcAreas(self):
      
        for i in range(len(self.fAM.views)):
            area = calcArea(len(self.fAM.views[i].coords),self.s)
            self.fAM.views[i].set_area(area) 
            self.totArea = self.totArea + area
