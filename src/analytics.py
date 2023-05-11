from helpers import calcArea, sameofViews,differenceofViews
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
    def calcAngles(self):
        x = 5
        #viewPerimeters = []
        #for i in range(len(self.fAM.views)):
            #do somethoing
            
            #vi = sameofViews(self.fAM.views[i].coords,self.perim)
            #viewPerimeters.append(vi)

        
        #print(len(self.perim))
        #for i in range(len(viewPerimeters[1])):
            #print("(", end = "")
            #print(viewPerimeters[1][i].getX(), end = ", ")
            #print(viewPerimeters[1][i].getY(), end = ")")
            #print("")
        #print("end of perimeter of view 1")

    def calcPerim(self):
        for i in range(len(self.fAM.lines)):
            x = len(self.fAM.lines[i]) - 1
            if(x < 0):
                continue
            self.perim.append(self.fAM.lines[i][x])

