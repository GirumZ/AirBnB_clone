#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
import datetime


class TestBaseModelClass(unittest.TestCase):
    """ Tests the BaseModel class"""

    def test_init_(self):
        """ Tests the constructer constructs form kwargs"""
        b = BaseModel()
        saved_as = b.to_dict()
        c = BaseModel(**saved_as)
        self.assertEqual(b.id, c.id)

    def test_id_type(self):
        """ Tests the type of id attribute"""
        b1 = BaseModel()
        self.assertIsInstance(b1.id, str)

    def test_id_uniqeness(self):
        """ Tests if id is unique for every object"""
        id_list = []
        for i in range(2000):
            b2 = BaseModel()
            self.assertNotIn(b2.id, id_list)
            id_list.append(b2.id)

    def test_created_at_type(self):
        """ Tests the type of created_at is datetime"""
        b3 = BaseModel()
        self.assertIsInstance(b3.created_at, datetime.datetime)

    def test_updated_at_type(self):
        """ Test the type of updated_at is datetime"""
        b4 = BaseModel()
        self.assertIsInstance(b4.updated_at, datetime.datetime)

    def test_created_and_updated_at_difference(self):
        """ Tests the time two instances are created is different"""
        b5 = BaseModel()
        b6 = BaseModel()

        self.assertNotEqual(b5.created_at, b6.created_at)

    def test_str_(self):
        """ Tests the representation of an object"""
        b7 = BaseModel()
        to_be_printed = "[{}] ({}) {}".format(b7.__class__.__name__,
                                              b7.id, b7.__dict__)
        self.assertEqual(str(b7), to_be_printed)

    def test_to_dict_type(self):
        """Tests to_dict returns a dictinary"""
        b9 = BaseModel()
        saved_as = b9.to_dict()
        self.assertIsInstance(saved_as, dict)

    def test_to_dict_content(self):
        """ Tests the content of dictinary from to_dict"""
        b10 = BaseModel()
        saved_as = b10.to_dict()

        self.assertIn("__class__", saved_as)
        self.assertIn("id", saved_as)
        self.assertIn("created_at", saved_as)
        self.assertIn("updated_at", saved_as)

    def test_to_dict_type(self):
        """ Tests the type of created_at and updated_at is str"""
        b11 = BaseModel()
        saved_as = b11.to_dict()
        for key, value in saved_as.items():
            if key == "created_at" or key == "updated at":
                self.assertIsInstance(value, str)

    def test_to_dict_new_attr(self):
        """ Tests if new attributes are added to the dictionary returned"""
        b12 = BaseModel()
        b12.purpose = "test"
        saved_as = b12.to_dict()

        self.assertIn("purpose", saved_as)


if __name__ == '__main__':
    unittest.main()
