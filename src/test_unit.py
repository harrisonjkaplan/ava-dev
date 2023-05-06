import unittest
from coord import Coord
from coord_field import CoordField
from graph import Graph
from haversine import haversine, Unit
from helpers import get_fake_elevations


class TestAVA(unittest.TestCase):
    def test_coord(self):
        c = Coord(1,2,3)
        self.assertEqual(c.getX(),1)
        self.assertEqual(c.getY(),2)
        self.assertEqual(c.getZ(),3)
        self.assertEqual(c.toString(),"(1, 2, 3)")

    def test_CoordField(self):
        step_size = .1
        cf = CoordField(75,75,1,step_size)
        cf.fillField()

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

    def test_helpers(self):
        elevations = get_fake_elevations(10)
        self.assertEqual(len(elevations),100)

