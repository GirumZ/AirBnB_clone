#!usr/bin/python3
""" A module that defines a class called Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """A class defination of Review"""

    place_id = ""
    user_id = ""
    text = ""
