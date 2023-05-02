from olympus import Olympus
from helpers import calcArea
#class for running multiple location analysis 
class Olympians:
    def __init__(self,xS,yS,h,r,s):
        self.xS = xS
        self.yS = yS
        self.h = h
        self.olys = []
        self.r = r
        self.s = s 
    
    def fillOlys(self):
        #print(len(self.xS))
        for i in range(len(self.xS)):
            self.olys.append(Olympus(self.xS[i],self.yS[i],self.h,self.r,self.s))
        for i in range(len(self.olys)):
            self.olys[i].grapher()

        
    def printAreas(self):
        x = 0

        
