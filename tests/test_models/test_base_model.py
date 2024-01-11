# File: tests/test_models/test_base_model.py

import unittest
from datetime import datetime  # Add this line
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):

    def test_id_creation(self):
        """ Test if id is created and is a string """
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_dates(self):
        """ Test if created_at, updated_at are datetime and set correctly """
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(model.created_at, model.updated_at)

    def test_save(self):
        """ Test if save updates updated_at """
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(model.updated_at, old_updated_at)

    def test_to_dict(self):
        """ Test to_dict method """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

if __name__ == '__main__':
    unittest.main()
