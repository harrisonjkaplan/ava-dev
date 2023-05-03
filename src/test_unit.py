import unittest
from coord import Coord
from coord_field import CoordField
from graph import Graph

class TestAVA(unittest.TestCase):
    def test_coord(self):
        c = Coord(1,2,3)
        self.assertEqual(c.getX(),1)
        self.assertEqual(c.getY(),2)
        self.assertEqual(c.getZ(),3)
        self.assertEqual(c.toString(),"(1, 2, 3)")

    def test_CoordField(self):
        cf = CoordField(0,0,.1,1)
        cf.fillField()

        self.assertEqual()

