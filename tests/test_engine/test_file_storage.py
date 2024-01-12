import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from unittest.mock import patch


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

    # Additional tests can be added here...


if __name__ == "__main__":
    unittest.main()
