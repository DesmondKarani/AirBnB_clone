#!/usr/bin/python3
"""
Unittest for State class
"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Define unittests for testing the State class."""

    def test_init(self):
        """Test initialization of State instance."""
        my_state = State()
        self.assertIsInstance(my_state, State)

    def test_attributes(self):
        """Test the attributes of State."""
        my_state = State()
        my_state.name = "California"
        self.assertEqual(my_state.name, "California")


if __name__ == '__main__':
    unittest.main()
