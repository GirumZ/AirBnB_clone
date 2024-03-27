#!/usr/bin/python3
""" Python module for the FileStorage class tests"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage
import unittest
import os
import json
import datetime


class TestFileStorageClass(unittest.TestCase):
    """ Tests for the FileStorage class"""

    def setUp(self):
        """ Sets up the testing environment"""

        self.model_1 = BaseModel()
        self.model_2 = BaseModel()
        self.model_3 = BaseModel()

    def test_BaseModel_save(self):
        """ Tests the BaseModel save method"""

        self.model_1.save()

        key = self.model_1.__class__.__name__ + "." + self.model_1.id
        self.assertEqual(storage._FileStorage__objects[key], self.model_1)
        self.assertIsInstance(self.model_1.id, str)
        self.assertIsInstance(self.model_1.created_at, datetime.datetime)
        self.assertIsInstance(self.model_1.updated_at, datetime.datetime)

    def test___file_path(self):
        """ Tests the __file_path attribute"""

        # checks if the __file_path attribute is a string
        self.assertIsInstance(storage._FileStorage__file_path, str)

    def test___objects(self):
        """ Tests the __objects attribute"""

        # checks if the __object attribute is a dictionary
        self.assertIsInstance(storage._FileStorage__objects, dict)

    def test_all(self):
        """ Tests the all method of the FileStorage class"""

        returned_value = storage.all()
        self.assertEqual(returned_value, storage._FileStorage__objects)

    def test_new(self):
        """ Tests the new method of the FileStorage class"""

        storage.new(self.model_1)
        key = self.model_1.__class__.__name__ + "." + self.model_1.id
        self.assertIn(key, storage._FileStorage__objects)
        self.assertEqual(storage._FileStorage__objects[key], self.model_1)

    def test_save(self):
        """ Tests the save method of the Filestorage class"""

        storage.new(self.model_1)
        storage.save()
        file_name = storage._FileStorage__file_path
        file_size = os.path.getsize(file_name)
        key = self.model_2.__class__.__name__ + "." + self.model_2.id
        with open(file_name, "r") as f:
            try:
                file_content = json.load(f)
                json_valid = True
            except json.JSONDecoderError:
                json_valid = False

        self.assertGreater(file_size, 0)
        self.assertTrue(json_valid)
        self.assertIsInstance(file_content, dict)
        self.assertEqual(file_content[key], storage._FileStorage__objects[key].to_dict())

if __name__ == '__main__':
    unittest.main()
