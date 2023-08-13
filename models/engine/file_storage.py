#!/usr/bin/python3
"""
This module provides the FileStorage class, which manages
the storage of objects in a JSON file.
TODO: we need to complete the description of the model here.
"""

import os
import json
from models.base_model import BaseModel


class FileStorage:
    """
    A class to manage the storage of objects in a JSON file.
        With the following attributes:
            __file_path: JSON file path
            __objects: a dictionary of objects (BaseModel)
    """

    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects currently stored.

        Return (dictionary): A dictionary (attribute __objects) containing
            all stored objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the storage (__objects), as the following
        format: ex: to store a BaseModel object with id=12121212,
        the key will be BaseModel.12121212)

        Args:
            obj (BaseModel): The object to be added to the storage.

        No_return_value.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """
        Saves the current state of the objects to the JSON file.

        No_return value.
        """
        with open(self.__file_path, "w", encoding="utf-8") as json_file:
            json.dump(self.__objects, json_file)

    def reload(self):
        """
        Loads the objects from the JSON file, if the file exists.
        Note: if the file does not  exist no exception is raised.

        No_return_value.
        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as json_file:
                FileStorage.__objects = json.load(json_file)
