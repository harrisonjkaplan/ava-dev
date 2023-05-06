import unittest
from coord import Coord
from coord_field import CoordField
from graph import Graph
from haversine import haversine, Unit
from helpers import get_fake_elevations
import random


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



    def test_helpers(self):
        elevations = get_fake_elevations(10)
        self.assertEqual(len(elevations),100)

