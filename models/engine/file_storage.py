#!/usr/bin/python3
""" This module defines the FileStorage class"""
import json
import os


class FileStorage():
    """ Class defination of FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns a dictionary containing all the BaseModel instances

            Returns:
                dict: dictionary containing all the objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id

            Args:
                obj: instance of a class
        """

        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""

        dictionary = {}
        for key, value in FileStorage.__objects.items():
            dictionary[key] = value.to_dict()

        with open(FileStorage.__file_path, "w") as f:
            json.dump(dictionary, f)

    def reload(self):
        """ deserializes the JSON file to __objects"""
        from models.base_model import BaseModel

        dic = {'BaseModel': BaseModel}

        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, "r") as f:
                data = json.load(f)
                for key, value in data.items():
                    self.new(dic[value['__class__']](**value))
