#!/usr/bin/python3
"""
Test suite for the BaseModel class in the models module.
Tests cover initialization, serialization, and storage integration.
"""


import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from unittest.mock import patch
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up method for FileStorage tests."""
        self.storage = FileStorage()
        self.test_model = BaseModel()
        self.test_model.name = "Test Model"
        self.test_model.my_number = 42
        self.test_model_json = self.test_model.to_dict()
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up tasks."""
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test if all returns the dictionary of objects."""
        self.assertEqual(len(self.storage.all()), 0)
        self.storage.new(self.test_model)
        self.assertEqual(len(self.storage.all()), 1)

    def test_new(self):
        """Test adding new object to storage."""
        self.storage.new(self.test_model)
        key = f"{self.test_model.__class__.__name__}.{self.test_model.id}"
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test saving objects to file."""
        self.storage.new(self.test_model)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as f:
            objs = json.load(f)
        self.assertIn(f"BaseModel.{self.test_model.id}", objs)

    def test_reload(self):
        """Test reloading objects from file."""
        self.storage.new(self.test_model)
        self.storage.save()
        self.storage.reload()
        key = f"BaseModel.{self.test_model.id}"
        self.assertIn(key, self.storage.all())

    @patch('models.engine.file_storage.FileStorage.save')
    def test_save_call(self, mock_save):
        """Test if save method is called in BaseModel's save."""
        self.test_model.save()
        mock_save.assert_called_once()

    def test_reload_no_file(self):
        """Test reload method when file doesn't exist."""
        try:
            os.remove(self.storage._FileStorage__file_path)
        except FileNotFoundError:
            pass
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_user_instance(self):
        """Test handling of User instances."""
        user = User()
        user.email = "user@example.com"
        user.password = "password"
        user.first_name = "John"
        user.last_name = "Doe"
        self.storage.new(user)
        self.storage.save()
        self.storage.reload()
        key = f"User.{user.id}"
        self.assertIn(key, self.storage.all())
        reloaded_user = self.storage.all()[key]
        self.assertEqual(reloaded_user.email, "user@example.com")

    def test_state_instance(self):
        """Test handling of State instances."""
        state = State()
        state.name = "California"
        self.storage.new(state)
        self.storage.save()
        self.storage.reload()
        key = f"State.{state.id}"
        self.assertIn(key, self.storage.all())

    def test_city_instance(self):
        """Test handling of City instances."""
        city = City()
        city.name = "San Francisco"
        city.state_id = "CA_01"
        self.storage.new(city)
        self.storage.save()
        self.storage.reload()
        key = f"City.{city.id}"
        self.assertIn(key, self.storage.all())
        reloaded_city = self.storage.all()[key]
        self.assertEqual(reloaded_city.name, "San Francisco")
        self.assertEqual(reloaded_city.state_id, "CA_01")

    def test_amenity_instance(self):
        """Test handling of Amenity instances."""
        amenity = Amenity()
        amenity.name = "Wifi"
        self.storage.new(amenity)
        self.storage.save()
        self.storage.reload()
        key = f"Amenity.{amenity.id}"
        self.assertIn(key, self.storage.all())
        reloaded_amenity = self.storage.all()[key]
        self.assertEqual(reloaded_amenity.name, "Wifi")

    def test_place_instance(self):
        """Test handling of Place instances."""
        place = Place()
        place.name = "My Place"
        place.city_id = "city_01"
        place.user_id = "user_01"
        place.description = "A cozy place"
        self.storage.new(place)
        self.storage.save()
        self.storage.reload()
        key = f"Place.{place.id}"
        self.assertIn(key, self.storage.all())
        reloaded_place = self.storage.all()[key]
        self.assertEqual(reloaded_place.name, "My Place")

    def test_review_instance(self):
        """Test handling of Review instances."""
        review = Review()
        review.place_id = "place_01"
        review.user_id = "user_01"
        review.text = "Great place!"
        self.storage.new(review)
        self.storage.save()
        self.storage.reload()
        key = f"Review.{review.id}"
        self.assertIn(key, self.storage.all())
        reloaded_review = self.storage.all()[key]
        self.assertEqual(reloaded_review.text, "Great place!")


if __name__ == "__main__":
    unittest.main()
