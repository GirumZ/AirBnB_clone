#!/usr/bin/python3
""" Test module for file_storage module"""
import os
import json
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
import models


class TestFileStorage(unittest.TestCase):
    """ Test for FileStorage class"""
    def setUp(self):
        """ Sets up the test environment"""
        self.storage = FileStorage()
        FileStorage._FileStorage__file_path = "test.json"
        FileStorage._FileStorage__objects = {}
        self.storage.reload()

    def tearDown(self):
        """ Cleansup after the test is complete"""
        if os.path.exists("test.json"):
            os.remove("test.json")

    def test_file_path(self):
        """ tests the existance and type of file path"""
        self.assertEqual(hasattr(FileStorage, "_FileStorage__file_path"), True)
        self.assertIsInstance(FileStorage._FileStorage__file_path, str)
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_objects(self):
        """ Tests the attribute __objects"""

        self.assertIsInstance(FileStorage._FileStorage__objects, dict)
        self.assertEqual(FileStorage._FileStorage__objects, {})

    def test_all_property(self):
        """ Tests the nethod all"""
        self.assertIsInstance(models.storage.all(), dict)
        self.assertEqual(self.storage.all(), {})

    def test_all_instance(self):
        """ Tests the all method with instances"""
        instance1 = BaseModel()
        self.assertEqual(self.storage.all(), {
            "BaseModel." + instance1.id: instance1
        })

    def test_new(self):
        """ Tests the method new"""
        n_dict = {
                'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                'created_at': '2017-09-28T21:03:54.052298',
                '__class__': 'BaseModel',
                'updated_at': '2017-09-28T21:03:54.052302'
        }

        k = "BaseModel.56d43177-cc5f-4d6c-a0c1-e167f8c27337"
        instance = BaseModel(**n_dict)
        self.storage.new(instance)
        self.assertIn(k, self.storage.all())
        self.assertIs(self.storage.all()[k], instance)

    def test_save(self):
        """ Tests the method save"""
        n_dict = {
                'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                'created_at': '2017-09-28T21:03:54.052298',
                '__class__': 'BaseModel',
                'updated_at': '2017-09-28T21:03:54.052302'
        }

        k = "BaseModel.56d43177-cc5f-4d6c-a0c1-e167f8c27337"
        saved_as = {k: n_dict}
        instance = BaseModel(**n_dict)
        self.storage.new(instance)
        self.storage.save()
        with open("test.json", "r") as f:
            got_dict = json.load(f)
            self.assertEqual(got_dict, saved_as)

    def test_reload(self):
        """ Tests the method reload"""
        n_dict = {
                'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                'created_at': '2017-09-28T21:03:54.052298',
                '__class__': 'BaseModel',
                'updated_at': '2017-09-28T21:03:54.052302'
        }

        k = "BaseModel.56d43177-cc5f-4d6c-a0c1-e167f8c27337"
        instance = BaseModel(**n_dict)
        self.storage.new(instance)
        self.storage.save()
        self.storage.reload()
        self.assertEqual(len(self.storage.all().keys()), 1)
        self.assertIn(k, self.storage.all())
        self.assertEqual(self.storage.all()[k].to_dict(), n_dict)


if __name__ == '__main__':
    unittest.main()
