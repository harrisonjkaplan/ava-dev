import math
class CoordField:##coord field takes in the startign coordinates and generates the grid of coordinates to 
    #be tested for elevation, with the starting x and y centered, it takes into account the current latitude 
    #when calculating the longitudinal distances 
    def __init__(self,x,y,r,s):
        self.x = x
        self.y = y
        self.r = r 
        self.s = s 
        self.xList = []
        self.yList = []
        self.num = r/s

    def fillField(self):
        degPerkilo = 1.0/111.0
        #xStep = self.s*degPerkilo
        #yStep=self.s*(1.0/(111.32*math.cos(math.radians(self.x))))
        yNew = self.y+(self.r*degPerkilo)
        xNew = self.x-round((self.r*1.0/(111.32*math.cos(math.radians(self.y)))),5) #calculating new latitiudes based on longitiude
        xO = xNew
        #print(self.num)
        for i in range(int(self.num*2-1)):
            
            for j in range(int(self.num*2-1)):
                self.xList.append(xNew)
                self.yList.append(yNew)
                xNew = round(xNew + (self.s*(1.0/(111.32*math.cos(math.radians(self.y))))),5)
         
            yNew = yNew - (self.s*degPerkilo)
  
            xNew = xO


