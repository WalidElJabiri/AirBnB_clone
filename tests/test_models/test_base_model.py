#!/usr/bin/env python3
"""
TestBaseModel: Test cases for the BaseModel class.
TODO: we need to complete the description of the model here
"""

import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    TestBaseModel class: Test cases for the BaseModel class.
    """

    def test_init(self):
        """
        Test_case_1: Test that id, created_at, and updated_at are initialized.
        Test_case_2: Test that id, created_at, and updated_at have the correct
        type.
        """
        obj = BaseModel()

        # Test_case_2
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))

        # Test_case_2
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)

    def test_to_dict(self):
        """
        Test_case_1: Test that to_dict method returns the expected dictionary
        Test_case_2: Test that '__class__', 'id', 'created_at', 'updated_at',
        have the correct type
        """
        obj = BaseModel()
        modified_dict = obj.to_dict()
        # Test_case_1
        self.assertIsInstance(modified_dict, dict)
        self.assertTrue('__class__' in modified_dict)
        self.assertTrue('id' in modified_dict)
        self.assertTrue('created_at' in modified_dict)
        self.assertTrue('updated_at' in modified_dict)

        # Test_case_2
        self.assertIsInstance(modified_dict['__class__'], str)
        self.assertIsInstance(modified_dict['id'], str)
        self.assertIsInstance(modified_dict['created_at'], str)
        self.assertIsInstance(modified_dict['updated_at'], str)

    def test_save(self):
        """
        Test updated_at attribute change upon invoking save
        """
        obj = BaseModel()
        old_updated_atribute = obj.updated_at
        obj.save()
        new_updated_updated_at = obj.updated_at
        self.assertNotEqual(old_updated_atribute, new_updated_updated_at)


if __name__ == '__main__':
    unittest.main()
