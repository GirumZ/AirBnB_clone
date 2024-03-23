#!/usr/bin/python3
""" tests for the BaseModel class attributes and methods"""

import unittest
from models.base_model import BaseModel


class TestBaseModelClass(unittest.TestCase):
    """ Class for testing the BaseModel class"""

    def setUp(self):
        """ sets up the test environment"""

        self.model_1 = BaseModel()
        self.model_2 = BaseModel()
        dict_source = self.model_2.to_dict()
        self.model_3 = BaseModel(**dict_source)

    def test___init__(self):
        """ Tests the constructor method of the BaseModel class"""

        # tests if the BaseModel instances are created
        self.assertIsInstance(self.model_1, BaseModel)
        self.assertIsInstance(self.model_2, BaseModel)
        self.assertIsInstance(self.model_3, BaseModel)

        # tests if the BaseModel instances are created using kwargs
        self.assertEqual(self.model_2.id, self.model_3.id)
        self.assertEqual(self.model_2.created_at, self.model_3.created_at)
        self.assertEqual(self.model_2.updated_at, self.model_3.updated_at)

    def test_id(self):
        """ Tests the id attribute of the BaseModel class"""

        # tests the uniqueness of id
        self.assertNotEqual(self.model_1.id, self.model_2.id)
        # tests if id attribute is a string
        self.assertIsInstance(self.model_1.id, str)

    def test_created_at(self):
        """ Tests the created_it attribute of the BaseModel class"""

        # tests the uniqueness of the created_at time of an object
        self.assertNotEqual(self.model_1.created_at, self.model_2.created_at)

    def test_updated_at(self):
        """ Tests the updated_at attribute of the BaseModel class"""

        # tests the uniqueness of the created_at time of an object
        self.assertNotEqual(self.model_1.updated_at, self.model_2.updated_at)

    def test___str__(self):
        """ Tests the string representation of a BaseModel object"""

        m_id = self.model_1.id
        m_name = self.model_1.__class__.__name__
        m_dict = self.model_1.__dict__

        needed_output = f"[{m_name}] ({m_id}) {m_dict}"

        # tests the string representation of a BaseModel object
        self.assertEqual(self.model_1.__str__(), needed_output)

    def test_save(self):
        """ Tests if the save method updates the updated_time attribute"""

        time_before = self.model_1.updated_at
        self.model_1.save()
        time_after = self.model_1.updated_at

        self.assertNotEqual(time_before, time_after)

    def test_to_dict(self):
        """ Tests the dictionary representation of an object"""

        dictionary = self.model_1.to_dict()

        # tests if the specific keys are present in the dictionary
        self.assertIn('id', dictionary)
        self.assertIn('created_at', dictionary)
        self.assertIn('updated_at', dictionary)
        self.assertIn('__class__', dictionary)

        # tests if the created_at and updated_at values are strings
        self.assertIsInstance(dictionary['created_at'], str)
        self.assertIsInstance(dictionary['updated_at'], str)
