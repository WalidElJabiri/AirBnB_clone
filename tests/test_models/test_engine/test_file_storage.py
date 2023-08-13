#!/usr/bin/python3
"""
TestFileStorage: Test cases for the FileStorage class.
TODO: we need to complete the description of the model here.
This unit test is full of shit at the moment.
"""

import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test cases for the FileStorage class.
    """
    total_object = 0

    def remove_file_if_exists(self):
        """
        Remove a JSON file if it exists.
        """
        if os.path.exists("storage.json"):
            os.remove("storage.json")

    def test_all(self):
        """
        Test that all() returns an empty dictionary initially.
        """
        storage_instance = FileStorage()
        self.assertIsInstance(storage_instance._FileStorage__objects, dict)
        # self.assertEqual(
        #    len(storage_instance._FileStorage__objects),
        #    TestFileStorage.total_object
        # )
        self.remove_file_if_exists()

    def test_new(self):
        """
        Test adding a new object and retrieving it with all().
        """
        storage_instance = FileStorage()
        obj = BaseModel()
        storage_instance.new(obj)
        TestFileStorage.total_object += 1
        objects = storage_instance.all()
        key = f"{obj.__class__.__name__}.{obj.id}"
        # self.assertEqual(len(objects), TestFileStorage.total_object)
        self.assertIn(key, objects)
        self.assertEqual(objects[key], obj.to_dict())
        self.remove_file_if_exists()

    def test_all(self):
        """
        Test adding a new object and retrieving it with all().
        """
        storage_instance = FileStorage()
        obj = BaseModel()
        storage_instance.new(obj)
        TestFileStorage.total_object += 1
        objects = storage_instance.all()
        key = f"{obj.__class__.__name__}.{obj.id}"
        # self.assertEqual(len(objects), TestFileStorage.total_object)
        self.assertIn(key, objects)
        self.assertEqual(objects[key], obj.to_dict())
        self.remove_file_if_exists()

    def test_save(self):
        """
        Test saving objects and reloading them.
        """
        # save to the storage
        storage_instance = FileStorage()
        obj1 = BaseModel()
        obj2 = BaseModel()
        storage_instance.new(obj1)
        key1 = f"{obj1.__class__.__name__}.{obj1.id}"
        TestFileStorage.total_object += 1
        storage_instance.new(obj2)
        key2 = f"{obj2.__class__.__name__}.{obj2.id}"
        TestFileStorage.total_object += 1
        storage_instance.save()

        # Reload from the storage
        new_storage = FileStorage()
        new_storage.reload()
        objects = new_storage.all()
        # self.assertEqual(len(objects), TestFileStorage.total_object)
        self.assertIn(key1, objects)
        self.assertEqual(objects[key1], obj1.to_dict())
        self.assertIn(key2, objects)
        self.assertEqual(objects[key2], obj2.to_dict())
        self.remove_file_if_exists()

    def test_reload(self):
        """
        Test saving objects and reloading them.
        """
        # save to the storage
        storage_instance = FileStorage()
        obj1 = BaseModel()
        obj2 = BaseModel()
        storage_instance.new(obj1)
        key1 = f"{obj1.__class__.__name__}.{obj1.id}"
        TestFileStorage.total_object += 1
        storage_instance.new(obj2)
        key2 = f"{obj2.__class__.__name__}.{obj2.id}"
        TestFileStorage.total_object += 1
        storage_instance.save()

        # Reload from the storage
        new_storage = FileStorage()
        new_storage.reload()
        objects = new_storage.all()
        # self.assertEqual(len(objects), TestFileStorage.total_object)
        self.assertIn(key1, objects)
        self.assertEqual(objects[key1], obj1.to_dict())
        self.assertIn(key2, objects)
        self.assertEqual(objects[key2], obj2.to_dict())
        self.remove_file_if_exists()


if __name__ == "__main__":
    unittest.main()
