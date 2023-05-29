class Coord:
#simple coord class to hold 3 dimensions
    def __init__(self,x,y,z):
        self.x = x 
        self.y = y 
        self.z = z 
        self.view = -1

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_z(self):
        return self.z
    def print_2d(self):
        print('(' + str(self.x) + ', ' + str(self.y) + ')')

    def to_string(self):
        return('(' + str(self.x) + ', ' + str(self.y)  + ', ' + str(self.z)+ ')')