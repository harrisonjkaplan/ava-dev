# from elevation_getter import ElevationGetter
from .coordinates import CoordField, Graph, View
from .viewshed import Viewshed
from .visualizer import Visualizer
from .helpers import reconcile_coords, get_fake_elevations, difference_of_views
#class to run the view shed for a single location
class Ava:
    def __init__(self,x,y,r,s,min_height=0,max_height=0):
        self.x = x
        self.y = y
        self.min_height = min_height 
        self.max_height = max_height
        self.r = r 
        self.s = s
        self.cf = CoordField(x,y,r,s)
        self.cf.fill_field()
     
        # self.ele = ElevationGetter(self.cf.longitude_list,self.cf.latitude_list)
        # self.elevations = self.ele.getElevation()
        self.elevations = get_fake_elevations(int((r/s)*2-1))
        self.graph = Graph(int(self.r/self.s),self.elevations,self.cf.longitude_list,self.cf.latitude_list)
        self.fams = []

    def getAPIReturnList(self):
        APIReturn = []

    
    def calc_viewsheds(self):
        for height in range(self.min_height,self.max_height+1):
            fam = Viewshed(self.graph,height,self.s)
            fam.run_franklin_and_ray()
            fam.calc_views()
            fam.set_area_of_views()
            self.fams.append(fam)
            if height == 0:
                fam.graph.update_new_coords(fam.vs)
            else:
                #will get the coords that are unique to this new height, assumes that all coords contained in previous height calculation will still be visible
                new_coords = difference_of_views(self.fams[height-self.min_height-1].vs,self.fams[height-self.min_height].vs)
                fam.graph.update_new_coords(new_coords)

    def get_areas(self):
        areas = []
        for fam in self.fams:
            areas.append(fam.get_area_of_views())
        return areas

            
    def visualize(self,areas,heights):
        xS = self.graph.x_list()
        yS = self.graph.y_list()
        zS = self.graph.z_list()
        xS2 = self.fams[0].x_list()
        yS2 = self.fams[0].y_list()
        zS2 = self.fams[0].z_list()

        v = Visualizer(xS,yS,zS,xS2,yS2,zS2,areas,heights)
        v.visualize()

    def get_response(self):
        response = {}
        observer = {
            "longitude": self.x,
            "latitude": self.y,
            "minumum_height": self.min_height,
            "maximum_height": self.max_height
        }
        viewshed_config = {
            "radius": self.r,
            "resolution": self.s
        }
        response['observer_details'] = observer
        response['viewshed_configuration'] = viewshed_config

        response['incremental_height_viewsheds'] = [fam.to_dict() for fam in self.fams]

        return response

