from haversine import inverse_haversine, Direction

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
    


