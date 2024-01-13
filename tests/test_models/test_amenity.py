#!/usr/bin/python3
"""
Unittest for Amenity class
"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_init(self):
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, Amenity)

    def test_attributes(self):
        my_amenity = Amenity()
        my_amenity.name = "Pool"
        self.assertEqual(my_amenity.name, "Pool")


if __name__ == '__main__':
    unittest.main()
