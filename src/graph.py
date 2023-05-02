from coord import Coord
class Graph: 
#takes in elevation data and returns a graph of points on easier x and y plots top right is -r, r elevation[0]

    def __init__(self,r,elevations,cf):
        self.r = r
        self.elevations = elevations
        self.g = []
        self.gList = []
       
        #Coords to use for bresenham and easier calculation
        x = 0
        for i in range(int(self.r*2)-1):
            yCoord = self.r-1-i
            newAdd = []
                #print("didthis")
            for j in range(int(self.r*2)-1):
                xCoord = j-self.r+1
                c = Coord(xCoord,-yCoord,elevations[x])
                x = x +1
                self.gList.append(c)
                    #c.print2d()
                newAdd.append(c)
            self.g.append(newAdd)


    

    def printXandY(self):
        for i in range(self.r*2-1):
            for j in range(self.r*2-1):
                #print("|  ", end = "  ")
                s = ""
                s = s + str(self.g[i][j].getX())
                s = s + ","
                s = s + str(self.g[i][j].getY())
                
                #print(s, end = " ")

            #print("")

    def xList(self):
        xS = []
        for i in range(self.r*2-1):
            for j in range(self.r*2-1):
                xS.append(self.g[i][j].getX())
        return xS 
    
    def yList(self):
        yS = []
        for i in range(self.r*2-1):
            for j in range(self.r*2-1):
                yS.append(self.g[i][j].getY())
        return yS 

    def zList(self):
        zS = []
        for i in range(self.r*2-1):
            for j in range(self.r*2-1):
                zS.append(self.g[i][j].getZ())
        return zS 
    