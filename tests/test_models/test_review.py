#!/usr/bin/python3
"""
Unittest for Review class
"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_init(self):
        my_review = Review()
        self.assertIsInstance(my_review, Review)

    def test_attributes(self):
        my_review = Review()
        my_review.place_id = "place_01"
        my_review.user_id = "user_01"
        my_review.text = "Great place, had a wonderful time!"
        self.assertEqual(my_review.place_id, "place_01")
        self.assertEqual(my_review.user_id, "user_01")
        self.assertEqual(my_review.text, "Great place, had a wonderful time!")


if __name__ == 'main':
    unittest.main()
