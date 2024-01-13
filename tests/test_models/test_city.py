#!/usr/bin/python3
"""
Unittest for City class
"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_init(self):
        my_city = City()
        self.assertIsInstance(my_city, City)

    def test_attributes(self):
        my_city = City()
        my_city.name = "San Francisco"
        my_city.state_id = "CA_01"
        self.assertEqual(my_city.name, "San Francisco")
        self.assertEqual(my_city.state_id, "CA_01")


if __name__ == '__main__':
    unittest.main()
