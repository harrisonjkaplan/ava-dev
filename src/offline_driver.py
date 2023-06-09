#in order for code to run, it needs to be run in the virtual environment 'venv'
from olympus import Olympus
from olympians import Olympians 
from analytics import Analytics
#driver of code


h = 1
r = 1
s = .1
oly = Olympus(37,-82,h,r,s)
oly.fAM.printViews()
areas = oly.multH(0,15)
heights = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]


### SEE HERE FOR WHAT API WILL RETURN
# api will return list of coordinates
#
#
###
#print(oly.gr1.gList)
returnList = oly.getAPIReturnList()
#for i in range(len(returnList)):
    #print(returnList[i].toString())



oly.visualize(areas,heights)

ana = Analytics(r,h,s,oly.fAM)
ana.calcPerim()
ana.calcAngles()
ana.calcAreas()
