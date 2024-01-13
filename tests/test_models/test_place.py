#!/usr/bin/python3
"""
Unittest for Place class
"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_init(self):
        my_place = Place()
        self.assertIsInstance(my_place, Place)

    def test_attributes(self):
        my_place = Place()
        my_place.city_id = "city_01"
        my_place.user_id = "user_01"
        my_place.name = "A nice place"
        my_place.description = "A cozy place with a nice view"
        my_place.number_rooms = 3
        my_place.number_bathrooms = 2
        my_place.max_guest = 4
        my_place.price_by_night = 100
        my_place.latitude = 37.7749
        my_place.longitude = -122.4194
        my_place.amenity_ids = ["amenity_01", "amenity_02"]
        self.assertEqual(my_place.city_id, "city_01")


if __name__ == '__main__':
    unittest.main()
