#!/usr/bin/python3
""" Test module for the State class"""


import unittest
from models.state import State
from models.base_model import BaseModel


class TestState_instances(unittest.TestCase):
    """ Tests for instances of state"""

    def test_state_inheritance(self):
        """ Tests the inheritance of a State instance"""

        instance = State()
        self.assertIsInstance(instance, State)
        self.assertIsInstance(instance, BaseModel)

    def test_state_attr_type(self):
        """ Tests the type of attributes of a State class instance"""

        instance = State()
        self.assertIsInstance(instance.name, str)


if __name__ == '__main__':
    unittest.main()
