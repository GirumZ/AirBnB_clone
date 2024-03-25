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
        """ Tests the save method of the FileStorage class"""

        storage.save()
        self.assertTrue(os.path.exists(storage._FileStorage__file_path))
        self.assertRegex(storage._FileStorage__file_path, r'\.json$')

    def test_reload(self):
        """ Tests the reload method of the FileStorage class"""

        key = self.model_2.__class__.__name__ + "." + self.model_2.id
        new_dict = {key: self.model_2.to_dict()}

        # manually creating the file.json file with model_2's data
        with open(storage._FileStorage__file_path, "w") as f:
            json.dump(new_dict, f)
        storage.reload()
        self.assertIn(key, storage._FileStorage__objects)


if __name__ == '__main__':
    unittest.main()
