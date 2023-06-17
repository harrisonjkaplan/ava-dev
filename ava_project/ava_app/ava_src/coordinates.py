from haversine import inverse_haversine, Direction

class Coord:
#simple coord class to hold 3 dimensions
    def __init__(self,x,y,z):
        self.x = x 
        self.y = y 
        self.z = z 
        self.view = -1

    def print_2d(self):
        print('(' + str(self.x) + ', ' + str(self.y) + ')')

    def to_string(self):
        return('(' + str(self.x) + ', ' + str(self.y)  + ', ' + str(self.z)+ ')')

class CoordField:##coord field takes in the startign coordinates and generates the grid of coordinates to 
    #be tested for elevation, with the starting x and y centered, it takes into account the current latitude 
    #when calculating the longitudinal distances 
    def __init__(self,x,y,r,s):
        self.x = x
        self.y = y
        self.r = r 
        self.s = s 
        self.longitude_list = []
        self.latitude_list = []
        self.num_steps = r/s

    def fill_field(self):
        for i in range(int(self.num_steps*2-1)):
            y_new,_ = inverse_haversine((self.y,self.x),self.s*(self.num_steps-1-i),Direction.NORTH)
            for j in range(int(self.num_steps*2-1)):
                _,x_new = inverse_haversine((self.y,self.x),self.s*(self.num_steps-1-j),Direction.WEST)

                self.longitude_list.append(x_new)
                self.latitude_list.append(y_new)
    
class Graph: 
#takes in elevation data and returns a graph of points on easier x and y plots top right is -r, r elevation[0]
    def __init__(self,num_steps,elevations):
        self.num_steps = num_steps
        self.elevations = elevations
        self.grid = []
        self.grid_list = []
       
        #Coords to use for bresenham and easier calculation
        coord_count = 0
        for i in range(int(self.num_steps*2)-1):
            y_val = self.num_steps-1-i
            row = []
            for j in range(int(self.num_steps*2)-1):
                x_val = j-self.num_steps+1
                new_coord = Coord(x_val,y_val,elevations[coord_count])
                coord_count = coord_count + 1
                self.grid_list.append(new_coord)
                row.append(new_coord)
            self.grid.append(row)

    def printXandY(self):
        for i in range(self.num_steps*2-1):
            s = f""
            for j in range(self.num_steps*2-1):
                s = s + f"({self.grid[i][j].x},{self.grid[i][j].y})"
            print(s)
                
    def x_list(self):
        xS = []
        for i in range(self.num_steps*2-1):
            for j in range(self.num_steps*2-1):
                xS.append(self.grid[i][j].x)
        return xS 
    
    def y_list(self):
        yS = []
        for i in range(self.num_steps*2-1):
            for j in range(self.num_steps*2-1):
                yS.append(self.grid[i][j].y)
        return yS 

    def z_list(self):
        zS = []
        for i in range(self.num_steps*2-1):
            for j in range(self.num_steps*2-1):
                zS.append(self.grid[i][j].z)
        return zS 
    
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
