import math 
from coord import Coord
from graph import Graph
from bresenham import bresenham
from view import View
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

#11/3
def reconcileCoords(gList,xList,yList,vs):
    #print(len(vs))
    realCoords = []

    for i in range(len(vs)):
        x = containsCoord2Index(vs[i],gList)
        c = Coord(xList[x],yList[x],gList[x].getZ())
        realCoords.append(c.toString())

    return realCoords


def calcArea(x,d):
    return d*d*x


def orderVS(vs,r):
    newVS = []
  
    yNum = -((r*2)-1)
    while(yNum <= r*2-1):
        xNum = -((r*2)-1)
        while(xNum <= r*2-1):
            c1 = Coord(xNum,yNum,0)
            index = containsCoord2Index(c1,vs)
            if(index == -1):
                xNum = xNum + 1
            else: 
                newVS.append(vs[index])
                xNum = xNum + 1
        yNum = yNum + 1
    return newVS


def dfs(vs,c1):
    coords = [c1]
    x = 1
    i = 0
    while(i<x):
        p1 = Coord(coords[i].getX()+1,coords[i].getY(),coords[i].getZ())
        p2 = Coord(coords[i].getX(),coords[i].getY()+1,coords[i].getZ())
        p3 = Coord(coords[i].getX()-1,coords[i].getY(),coords[i].getZ())
        p4 = Coord(coords[i].getX(),coords[i].getY()-1,coords[i].getZ())
        if(containsCoord2(p1,vs) == True and containsCoord2(p1,coords) == False):
            x = x + 1
            coords.append(p1)
        if(containsCoord2(p2,vs) == True and containsCoord2(p2,coords) == False):
            x = x + 1
            coords.append(p2)
        if(containsCoord2(p3,vs) == True and containsCoord2(p3,coords) == False):
            x = x + 1
            coords.append(p3)
        if(containsCoord2(p4,vs) == True and containsCoord2(p4,coords) == False):
            x = x + 1
            coords.append(p4)
        i = i +1
    return coords


def getString(coords):
    s = ""
    for i in range(len(coords)):
        s = s + coords[i]
    return s
def countString(sArray):
    count = 0 
    
    for i in range (len(sArray)):
        if(sArray[i]!= []):
        
            count = count + 1
    return count 
def coordsString(lats,longs):
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

def coordsSmasher(lats, longs,numCoords):
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


def xList(vs):
    xS = []
    for i in range(len(vs)):
        xS.append(vs[i].getX())
    return xS
def yList(vs):
    yS = []
    for i in range(len(vs)):
        yS.append(vs[i].getY())
    return yS
def zList(vs):
    zS = []
    for i in range(len(vs)):
        zS.append(vs[i].getZ())
    return zS
def bres(g,c1,c2,r):
    #print(c2.getX())

    x1 = c1.getX()
    x2 = c2.getX()
    y1 = c1.getX()
    y2 = c2.getY()
    coordsList = list(bresenham(x1,y1,x2,y2))
    coords = []
  
    for i in range(len(coordsList)):
        c = Coord(coordsList[i][0],coordsList[i][1],getElevation(g,coordsList[i],r))
        coords.append(c)
    return coords


def getElevation(g,coord,r):
    for i in range(r*2-1):
        for j in range(r*2-1):
            if(g[i][j].getX() == coord[0]):
                if (g[i][j].getY() == coord[1]):
                    return g[i][j].getZ()
def containsCoord(g,c2,r):
    
    for i in range (r*2-1):
        for j in range(r*2-1):
            c1 = g[i][j]
            
            if(coordsEqual(c1,c2)):
                return True
    return False
def adjacentPointCheck(c1,views):
    p1 = Coord(c1.getX()+1,c1.getY(),c1.getZ())
    p2 = Coord(c1.getX(),c1.getY()+1,c1.getZ())
    p3 = Coord(c1.getX()-1,c1.getY(),c1.getZ())
    p4 = Coord(c1.getX(),c1.getY()-1,c1.getZ())
    if(containsCoord2(p1,views) == True):
        return True
    if(containsCoord2(p2,views) == True):
        return True
    if(containsCoord2(p3,views) == True):
        return True
    if(containsCoord2(p4,views) == True):
        return True
    
    return False
    
def containsCoord2(c2,coords):
    for i in range(len(coords)):
        if(coordsEqual(c2,coords[i])):
            return True
    return False
def containsCoord2Index(c2,coords):
    for i in range(len(coords)):
        if(coordsEqual(c2,coords[i])):
            return i
    return -1

def viewHasCoord(coords1,coords2):
    for i in range(len(coords2)):
        for j in range(len(coords1)):
            if(coordsEqual(coords1[j],coords2[i]) == True):
                return True
def differenceofViews(v1,vs):
    coords = []
    for i in range(len(vs)):
        check = False
        for j in range(len(v1)):
            
            if(coordsEqual(v1[j],vs[i]) == True):
                check = True
        if(check== False):
            coords.append(vs[i])

    return coords
def sameofViews(v1,vs):
    coords = []
    for i in range(len(vs)):
        check = False
        for j in range(len(v1)):
            if(coordsEqual(v1[j],vs[i]) == True):
                check = True
        if(check== True):
            coords.append(vs[i])

    return coords

            

def addView(v1,v2):
    for i in range(len(v2.coords)):
        v1.addCoord(v2.coords[i])
    return False
def coordsEqual(c1,c2):
    if c1.getX() == c2.getX():
        
        if c1.getY() == c2.getY():

            return True
        else:
            return False
    else:   
        return False


def slope(c1,c2,h):
    
    return (c2.getZ()-(c1.getZ()+h)) /math.sqrt(((c2.getX()- c1.getX()) ** 2 + (c2.getY()- c1.getY()) ** 2))

def getPerimeter(gr1):
    cells = []
    #get top row 
    for i in range(gr1.r*2-1):
        #print(gr1.g[0][i].getX(), end = ", ")
       # print(gr1.g[0][i].getY())
        cells.append(gr1.g[0][i])
    #get bottom row 
    for i in range(gr1.r*2-1):
        cells.append(gr1.g[gr1.r*2-2][i])
       # print(gr1.g[r*2-2][i].getX(), end = ", ")
        #print(gr1.g[r*2-2][i].getY())
    #get left column 
    for i in range(1, gr1.r*2-2):
        cells.append(gr1.g[i][0])
       # print(gr1.g[i][0].getX(), end = ", ")
       # print(gr1.g[i][0].getY())
    for i in range(1, gr1.r*2-2):
        cells.append(gr1.g[i][gr1.r*2-2])

    return cells 
    
    
