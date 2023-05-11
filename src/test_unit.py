import unittest
from coord import Coord
from coord_field import CoordField
from graph import Graph
from haversine import haversine, Unit
from helpers import get_fake_elevations, get_perimeter, contains_coord, coords_equal, contains_coord_index
import random
from franklin_and_ray import FranklinAndRay
from view import View


class TestAVA(unittest.TestCase):
    def test_coord(self):
        c = Coord(1,2,3)
        self.assertEqual(c.get_x(),1)
        self.assertEqual(c.get_y(),2)
        self.assertEqual(c.get_z(),3)
        self.assertEqual(c.to_string(),"(1, 2, 3)")

    def test_CoordField(self):
        step_size = .1
        cf = CoordField(75,75,1,step_size)
        cf.fill_field()

        self.assertEqual(cf.num_steps,10)

        self.assertEqual(len(cf.longitude_list),361)
        self.assertEqual(len(cf.latitude_list),361)

        dist1 = haversine((cf.latitude_list[0],cf.longitude_list[0]),(cf.latitude_list[1],cf.longitude_list[1]))
        dist2 = haversine((cf.latitude_list[0],cf.longitude_list[0]),(cf.latitude_list[19],cf.longitude_list[19]))

        dist1_diff = abs(dist1-step_size)
        dist2_diff = abs(dist2-step_size)

        #Within a 9 centimeters of error
        self.assertEqual(dist1_diff<.0009,True)
        self.assertEqual(dist2_diff<.0009,True)
    
    def test_graph(self):
        num_steps = 5
        random_elevations = [random.randint(0, 10) for _ in range((num_steps*2-1)**2)]
        g = Graph(num_steps,random_elevations)

        self.assertEqual(len(g.grid),num_steps*2-1)
        self.assertEqual(len(g.grid[0]),num_steps*2-1)

        self.assertEqual(g.grid[0][0].get_z(),random_elevations[0])
        self.assertEqual(g.grid[-1][-1].get_z(),random_elevations[-1])

        fake_x_list = [-4, -3, -2, -1, 0, 1, 2, 3, 4, -4, -3, -2, -1, 0, 1, 2, 3, 4, -4, -3, -2, -1, 0, 1, 2, 3, 4, -4, -3, -2, -1, 0, 1, 2, 3, 4, -4, -3, -2, -1, 0, 1, 2, 3, 4, -4, -3, -2, -1, 0, 1, 2, 3, 4, -4, -3, -2, -1, 0, 1, 2, 3, 4, -4, -3, -2, -1, 0, 1, 2, 3, 4, -4, -3, -2, -1, 0, 1, 2, 3, 4]
        fake_y_list = [4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4]
        self.assertEqual(g.x_list(),fake_x_list)
        self.assertEqual(g.y_list(),fake_y_list)
        self.assertEqual(g.z_list(),random_elevations)

    def test_franklin_and_ray(self):
        #Fake elevations where I know the vs

        #all are visible
        ele_vals = [2,2,2,2,2,
                    2,1,1,1,2,
                    2,1,0,1,2,
                    2,1,1,1,2,
                    2,2,2,2,2]
        
        graph = Graph(3,ele_vals)
        fam = FranklinAndRay(graph, 0)
        self.assertEqual(len(graph.grid),5)
        fam.runFranklinAndRay()
        self.assertEqual(len(fam.vs),24)

        #some missing points
        ele_vals = [0,2,2,2,2,
                    2,1,1,1,0,
                    2,1,0,1,2,
                    2,1,1,1,2,
                    2,2,0,2,2]
        
        graph = Graph(3,ele_vals)
        fam = FranklinAndRay(graph, 0)
        self.assertEqual(len(graph.grid),5)
        fam.runFranklinAndRay()
        self.assertEqual(len(fam.vs),21)

        #making sure the 3 missing coords are not in the vs
        self.assertFalse(contains_coord(Coord(-2,2,0),fam.vs))
        self.assertFalse(contains_coord(Coord(2,1,0),fam.vs))
        self.assertFalse(contains_coord(Coord(0,-2,0),fam.vs))

        #testing calc_views
        fam.calc_views()
        

    def test_view(self):
        c1 = Coord(1,2,3)
        c2 = Coord(4,5,6)
        v = View()

        v.add_coords([c1,c2])
        self.assertEqual(len(v.coords),2)
        v.set_area(25.5)
        self.assertEqual(v.area,25.5)

    def test_helpers(self):
        #test get_fake_elevations
        elevations = get_fake_elevations(10)
        self.assertEqual(len(elevations),100)

        #test get_perimeter
        ele_vals = [2,2,2,2,2,
                    2,1,1,1,2,
                    2,1,0,1,2,
                    2,1,1,1,2,
                    2,2,2,2,2]
        
        graph = Graph(3,ele_vals)
        perimeter = get_perimeter(graph)
        self.assertEqual((len(perimeter)),16)
        self.assertEqual(perimeter[0].get_x(),-2)
        self.assertEqual(perimeter[4].get_x(),2)
        self.assertEqual(perimeter[6].get_x(),-1)
        self.assertEqual(perimeter[15].get_x(),2)
        self.assertEqual(perimeter[0].get_y(),2)
        self.assertEqual(perimeter[4].get_y(),2)
        self.assertEqual(perimeter[6].get_y(),-2)
        self.assertEqual(perimeter[15].get_y(),-1)

        #test coords equal and contains coord
        c1 = Coord(1,2,3)
        c2 = Coord(4,5,6)
        c3 = Coord(1,2,3)
        c4 = Coord(7,8,9)

        self.assertTrue(coords_equal(c1,c3))
        self.assertFalse(coords_equal(c1,c2))
        coords_list = [c1,c2,c3]
        self.assertTrue(contains_coord(c1,coords_list))
        self.assertFalse(contains_coord(c4,coords_list))
        self.assertEqual(contains_coord_index(c1,coords_list),0)
        self.assertEqual(contains_coord_index(c4,coords_list),-1)









