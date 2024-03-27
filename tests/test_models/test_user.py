#!/usr/bin/python3
""" Test module for the User class"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser_instances(unittest.TestCase):
    """ Tests for instances of user"""

    def test_user_attr_type(self):
        """ Tests the type of attributes"""
        instance = User()
        self.assertIsInstance(instance.email, str)
        self.assertIsInstance(instance.password, str)
        self.assertIsInstance(instance.first_name, str)
        self.assertIsInstance(instance.last_name, str)

    def test_user_inheritance(self):
        """ Tests the class of an instance"""
        instance = User()
        self.assertIsInstance(instance, User)
        self.assertIsInstance(instance, BaseModel)


if __name__ == '__main__':
    unittest.main()
