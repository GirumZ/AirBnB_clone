#!/usr/bin/python3
""" Test module for the place class"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class Testplace_instances(unittest.TestCase):
    """ Tests for instances of place"""

    def test_place_inheritance(self):
        """ Tests the inheritance of a place instance"""

        instance = Place()
        self.assertIsInstance(instance, Place)
        self.assertIsInstance(instance, BaseModel)

    def test_place_attr_type(self):
        """ Tests the types of attributes in place instance"""

        instance = Place()
        self.assertIsInstance(instance.city_id, str)
        self.assertIsInstance(instance.user_id, str)
        self.assertIsInstance(instance.name, str)
        self.assertIsInstance(instance.description, str)
        self.assertIsInstance(instance.number_rooms, int)
        self.assertIsInstance(instance.number_bathrooms, int)
        self.assertIsInstance(instance.max_guest, int)
        self.assertIsInstance(instance.price_by_night, int)
        self.assertIsInstance(instance.latitude, float)
        self.assertIsInstance(instance.longitude, float)
        self.assertIsInstance(instance.amenity_ids, list)


if __name__ == '__main__':
    unittest.main()
