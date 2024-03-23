#!/usr/bin/python3
""" A module for the defination of the BaseModel class"""
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ Defination of the BaseModel class"""

    def __init__(self):
        """ constructor method for the BaseModel class"""

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ formats the string representation of a class instance

            Returns:
                str: the string representation of a class instance
        """

        string = f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
        return string

    def save(self):
        """ Updates the attribute updated_at to the current time """

        self.updated_at = datetime.now()

    def to_dict(self):
        """ Returns a dictionary containing all keys/values of __dict__

            Returns:
                dict: all keys/values of __dict__
                with __class__.__name__ included
                """

        dictinary = self.__dict__
        # to change created_at and updated_at to strings
        dictinary['created_at'] = self.created_at.isoformat()
        dictinary['updated_at'] = self.updated_at.isoformat()
        # to add the class name to the dictinary
        dictinary["__class__"] = self.__class__.__name__
        return dictinary
