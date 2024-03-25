#!/usr/bin/python3
""" Imports the FileStorage class and initialize an instance"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
