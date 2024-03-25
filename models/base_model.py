#!/usr/bin/python3
""" A module for the defination of the BaseModel class"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel():
    """ Defination of the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """ constructor method for the BaseModel class"""

        # If a dictionary is given
        expected_format = "%Y-%m-%dT%H:%M:%S.%f"
        if (kwargs):
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(kwargs[key], expected_format)
                if key != '__class__':
                    setattr(self, key, value)
        else:
            # If no dictionary is given
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ formats the string representation of a class instance

            Returns:
                str: the string representation of a class instance
        """

        string = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return string

    def save(self):
        """ Updates the attribute updated_at to the current time
        """

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__

            Returns:
                dict: all keys/values of __dict__
                with __class__.__name__ included
                """

        dictinary = self.__dict__.copy()
        # to change created_at and updated_at to strings
        dictinary['created_at'] = self.created_at.isoformat()
        dictinary['updated_at'] = self.updated_at.isoformat()
        # to add the class name to the dictinary
        dictinary["__class__"] = self.__class__.__name__
        return dictinary
