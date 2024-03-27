#!/usr/bin/python3
""" Test module for the Amenity class"""

import unittest
from models.amenity import Amenity


class TestAmenity_instances(unittest.TestCase):
    """ Tests for instances of amenity"""

    def test_amenity_instances(self):
        """ Tests the instances of the class amenity"""

        instance = Amenity()
        self.assertIsInstance(instance.name, str)

    def test_amenity_inheritance(self):
        """ Tests the inheritance of an instance"""

        instance = Amenity()
        self.assertIsInstance(instance, Amenity)
        self.assertIsInstance(instance, Amenity)


if __name__ == '__main__':
    unittest.main()
