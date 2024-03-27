#!/usr/bin/python3
""" Test module for the city class"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity_instances(unittest.TestCase):
    """ Tests for instances of City"""

    def test_city_inheritance(self):
        """ Tests the inheritance of the City class"""

        instance = City()
        self.assertIsInstance(instance, City)
        self.assertIsInstance(instance, BaseModel)

    def test_city_attr_type(self):
        """ Testts the type of attribute of a City class instance"""

        instance = City()
        self.assertIsInstance(instance.state_id, str)
        self.assertIsInstance(instance.name, str)


if __name__ == '__main__':
    unittest.main()
