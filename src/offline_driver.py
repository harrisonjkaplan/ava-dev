#in order for code to run, it needs to be run in the virtual environment 'venv'
from ava import Ava

#driver of code


min_height = 0
max_height = 6
r = 3
s = 1
ava = Ava(37,-82,r,s,min_height,max_height)
ava.calc_viewsheds()

areas = [fam.total_vs_area for fam in ava.fams]


### SEE HERE FOR WHAT API WILL RETURN
# api will return list of coordinates
#
#
###
#print(oly.graph.gList)
returnList = ava.getAPIReturnList()
#for i in range(len(returnList)):
    #print(returnList[i].toString())


height_range =list(range(min_height, max_height+1))
print(height_range)

print(f"areas: {areas}")
ava.visualize(areas,height_range)