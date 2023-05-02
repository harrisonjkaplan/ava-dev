class Coord:
#simple coord class to hold 3 dimensions
    def __init__(self,x,y,z):
        self.x = x 
        self.y = y 
        self.z = z 

    

    def getX(self):
        
        return self.x
    def getY(self):
        return self.y
    def getZ(self):
        return self.z
    def print2d(self):
        print('(' + str(self.x) + ', ' + str(self.y) + ')')

    def toString(self):
        return('(' + str(self.x) + ', ' + str(self.y)  + ', ' + str(self.z)+ ')')