from coord import Coord
#classification of viewpoints, a view is comprosed of points that are all ajacent 
class View: 
    def __init__(self):
        self.coords = []
        self.area = 0
    def add_coords(self,c):
        for i in range(len(c)):
            self.coords.append(c[i])
    def set_area(self,a):
        self.area = a

    def get_coords(self):
        for i in range(len(self.coords)):
            self.coords[i].print2d()
