#!/usr/bin/python3
""" Test module for the Review class"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview_instances(unittest.TestCase):
    """ Tests for instances of review"""

    def test_review_inheritance(self):
        """ Tests the inheritance of a Review class"""

        instance = Review()
        self.assertIsInstance(instance, Review)
        self.assertIsInstance(instance, BaseModel)

    def test_review_attr_type(self):
        """ Tests the type of attributes for a Review class"""

        instance = Review()
        self.assertIsInstance(instance.place_id, str)
        self.assertIsInstance(instance.user_id, str)
        self.assertIsInstance(instance.text, str)


if __name__ == '__main__':
    unittest.main()
