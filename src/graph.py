from coord import Coord
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
                s = s + f"({self.grid[i][j].get_x()},{self.grid[i][j].get_y()})"
            print(s)
                
    def x_list(self):
        xS = []
        for i in range(self.num_steps*2-1):
            for j in range(self.num_steps*2-1):
                xS.append(self.grid[i][j].get_x())
        return xS 
    
    def y_list(self):
        yS = []
        for i in range(self.num_steps*2-1):
            for j in range(self.num_steps*2-1):
                yS.append(self.grid[i][j].get_y())
        return yS 

    def z_list(self):
        zS = []
        for i in range(self.num_steps*2-1):
            for j in range(self.num_steps*2-1):
                zS.append(self.grid[i][j].get_z())
        return zS 
    