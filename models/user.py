#!/usr/bin/python3
"""A module defining a class called User"""

from models.base_model import BaseModel


class User(BaseModel):
    """Defination of the class User"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
