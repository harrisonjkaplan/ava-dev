import math 
from .coordinates import Coord, View
from bresenham import bresenham
from hkb_diamondsquare import DiamondSquare as DS

#file containing all helper methods used in other classes
def get_fake_elevations(size):
    #roughness val can be > 0 and < 1
    fake_elevations = DS.diamond_square(shape=(size,size), 
                         min_height=1, 
                         max_height=25,
                         roughness=0.01)
    fake_ele_vals = []
    for i in range(len(fake_elevations)):
        for j in range(len(fake_elevations[i])):
            fake_ele_vals.append(fake_elevations[i][j])
    return fake_ele_vals

def reconcile_coords(gList,xList,yList,vs):
    realCoords = []

    for i in range(len(vs)):
        x = contains_coord_index(vs[i],gList)
        c = Coord(xList[x],yList[x],gList[x].z)
        realCoords.append(c.to_string())

    return realCoords

def order_vs(vs,r):
    ordered_vs = []
  
    y = -((r*2)-1)
    while(y <= r*2-1):
        x = -((r*2)-1)
        while(x <= r*2-1):
            c1 = Coord(x,y,0)
            index = contains_coord_index(c1,vs)
            if(index == -1):
                x = x + 1
            else: 
                ordered_vs.append(vs[index])
                x = x + 1
        y = y + 1
    return ordered_vs


def dfs(vs,c1):
    coords = [c1]
    x = 1
    i = 0
    while(i<x):
        p1 = Coord(coords[i].x+1,coords[i].y,coords[i].z,0,0)
        p2 = Coord(coords[i].x,coords[i].y+1,coords[i].z)
        p3 = Coord(coords[i].x-1,coords[i].y,coords[i].z)
        p4 = Coord(coords[i].x,coords[i].y-1,coords[i].z)
        if(contains_coord(p1,vs) == True and contains_coord(p1,coords) == False):
            x = x + 1
            coords.append(p1)
        if(contains_coord(p2,vs) == True and contains_coord(p2,coords) == False):
            x = x + 1
            coords.append(p2)
        if(contains_coord(p3,vs) == True and contains_coord(p3,coords) == False):
            x = x + 1
            coords.append(p3)
        if(contains_coord(p4,vs) == True and contains_coord(p4,coords) == False):
            x = x + 1
            coords.append(p4)
        i = i +1
    return coords


def get_string(coords):
    s = ""
    for i in range(len(coords)):
        s = s + coords[i]
    return s
def count_string(sArray):
    count = 0 
    
    for i in range (len(sArray)):
        if(sArray[i]!= []):
        
            count = count + 1
    return count 
def coords_string(lats,longs):
    sArray = [[],[],[],[],[],[]]
    size = len(lats)
    count = 0

    for i in range(len(sArray)):
        for j in range(300):
            #print(i)
            if(300-1== j or len(longs)-1 == count):
                s = ""
                s = s + str(lats[count]) + "," + str(longs[count])
                sArray[i].append(s) 
            else:
                s = ""
                s = s + str(lats[count]) + "," + str(longs[count]) + "| "
                sArray[i].append(s) 
            count = count +1
           
            if(count == len(lats)):
                break
        if(count == len(lats)):
            break

    return sArray

def coords_smasher(lats, longs,numCoords):
    sArray = []
    numCalls = int(numCoords/300) +1
    for i in range(1):
            sArray.append("")
            #print("done")

    x = len(sArray)

    count = 0
    for i in range(x): 
            for j  in range(121):
                    sArray[i] = sArray[i] + str(lats[count]) + "," + str(longs[count])
                    count = count +1
                    if (121!=j+1):
                     sArray[i] = sArray[i] + '|'
    return sArray

def bres(g,c1,c2,num_steps):
    x1 = c1.x
    x2 = c2.x
    y1 = c1.y
    y2 = c2.y
    coords_list = list(bresenham(x1,y1,x2,y2))
    coords = []
  
    for i in range(len(coords_list)):
        c = Coord(coords_list[i][0],coords_list[i][1],get_elevation(g,coords_list[i],num_steps))
        coords.append(c)
    return coords

def get_elevation(g,coord,r):
    for i in range(r*2-1):
        for j in range(r*2-1):
            if(g[i][j].x == coord[0]) and (g[i][j].y == coord[1]):
                return g[i][j].z
def contains_coord(g,c2,r):
    
    for i in range (r*2-1):
        for j in range(r*2-1):
            c1 = g[i][j]
            
            if(coords_equal(c1,c2)):
                return True
    return False
def adjacent_point_check(c1,views):
    p1 = Coord(c1.x+1,c1.y,c1.z)
    p2 = Coord(c1.x,c1.y+1,c1.z)
    p3 = Coord(c1.x-1,c1.y,c1.z)
    p4 = Coord(c1.x,c1.y-1,c1.z)
    if(contains_coord(p1,views) == True):
        return True
    if(contains_coord(p2,views) == True):
        return True
    if(contains_coord(p3,views) == True):
        return True
    if(contains_coord(p4,views) == True):
        return True
    
    return False
    
def contains_coord(coord,coords_list):
    for i in range(len(coords_list)):
        if(coords_equal(coord,coords_list[i])):
            return True
    return False

def contains_coord_index(coord,coords_list):
    for i in range(len(coords_list)):
        if(coords_equal(coord,coords_list[i])):
            return i
    return -1

def view_has_coord(coords1,coords2):
    for i in range(len(coords2)):
        for j in range(len(coords1)):
            if(coords_equal(coords1[j],coords2[i]) == True):
                return True
            
def difference_of_views(view,vs):
    '''Returns the coords contained in vs that are not in view'''
    coords = []
    for i in range(len(vs)):
        check = False
        for j in range(len(view)):
            
            if(coords_equal(view[j],vs[i]) == True):
                check = True
        if(check== False):
            coords.append(vs[i])

    return coords

def intersection_of_views(view,vs):
    '''Contains the coords that are in both view and vs'''
    coords = []
    for i in range(len(vs)):
        check = False
        for j in range(len(view)):
            if(coords_equal(view[j],vs[i]) == True):
                check = True
        if(check== True):
            coords.append(vs[i])

    return coords

def coords_equal(c1,c2):
    if c1.x == c2.x and c1.y == c2.y:
        return True
    else:
        return False

def slope(c1,c2,h):
    return (c2.z-(c1.z+h)) /math.sqrt(((c2.x- c1.x) ** 2 + (c2.y- c1.y) ** 2))

def get_perimeter(graph):
    perimeter_coords = []
    #get top row 
    for i in range(graph.num_steps*2-1):
        perimeter_coords.append(graph.grid[0][i])
    #get bottom row 
    for i in range(graph.num_steps*2-1):
        perimeter_coords.append(graph.grid[graph.num_steps*2-2][i])

    #get left column 
    for i in range(1, graph.num_steps*2-2):
        perimeter_coords.append(graph.grid[i][0])

    for i in range(1, graph.num_steps*2-2):
        perimeter_coords.append(graph.grid[i][graph.num_steps*2-2])

    return perimeter_coords 
    
    
