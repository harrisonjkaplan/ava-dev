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
        # self.elevations = get_fake_elevations(int((r/s)*2-1))
        self.elevations = [0,1,1,0,1,1,1,
                    1,0,0,0,0,0,1,
                    1,0,1,1,1,0,1,
                    0,0,1,0,1,0,0,
                    1,0,1,1,1,0,1,
                    1,0,0,0,0,0,1,
                    1,1,0,0,1,1,1]
        self.fams = []
        self.graphs = []
        for i in range(self.min_height,self.max_height+1):
            graph = Graph(int(self.r/self.s),self.elevations,self.cf.longitude_list,self.cf.latitude_list)
            print(id(graph))
            self.graphs.append(graph)
            
    def calc_viewsheds(self):
        i = 0
        for height in range(self.min_height,self.max_height+1):
            fam = Viewshed(self.graphs[i],height,self.s)
            fam.run_franklin_and_ray()
            fam.calc_views()
            fam.set_area_of_views()
            print(height)
            if height == 0:
                fam.graph.update_new_coords(fam.vs)
            else:
                #will get the coords that are unique to this new height, assumes that all coords contained in previous height calculation will still be visible
                new_coords = difference_of_views(self.fams[i-1].vs,fam.vs)
                fam.graph.update_new_coords(new_coords)

            self.fams.append(fam)
            i=+1

    def get_areas(self):
        areas = []
        for fam in self.fams:
            areas.append(fam.get_area_of_views())
        return areas

            
    # def visualize(self,areas,heights):
    #     xS = self.graph.x_list()
    #     yS = self.graph.y_list()
    #     zS = self.graph.z_list()
    #     xS2 = self.fams[0].x_list()
    #     yS2 = self.fams[0].y_list()
    #     zS2 = self.fams[0].z_list()

    #     v = Visualizer(xS,yS,zS,xS2,yS2,zS2,areas,heights)
    #     v.visualize()

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

