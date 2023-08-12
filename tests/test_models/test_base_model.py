#!/usr/bin/python3
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
        The folowing test cases would check both:
            1.new instance
            2.and Reconstructed one
        Test_case_1: Test that id, created_at, and updated_at are initialized.
        Test_case_2: Test that id, created_at, and updated_at have the correct
        type.
        """
        obj = BaseModel()
        reconstructed_obj = BaseModel(**(obj.to_dict()))
        # Test_case_1: new instance
        self.assertTrue(hasattr(obj, 'id'))
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertTrue(hasattr(obj, 'updated_at'))
        # Test_case_1: reconstructed instance
        self.assertTrue(hasattr(reconstructed_obj, 'id'))
        self.assertTrue(hasattr(reconstructed_obj, 'created_at'))
        self.assertTrue(hasattr(reconstructed_obj, 'updated_at'))
        # Test_case_2: new instance
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime.datetime)
        self.assertIsInstance(obj.updated_at, datetime.datetime)
        # Test_case_2: reconstructed instance
        self.assertIsInstance(reconstructed_obj.id, str)
        self.assertIsInstance(reconstructed_obj.created_at, datetime.datetime)
        self.assertIsInstance(reconstructed_obj.updated_at, datetime.datetime)

    def test_to_dict(self):
        """
        The folowing test cases would check both:
            1.new instance
            2.and Reconstructed one
        Test_case_1: Test that to_dict method returns the expected dictionary
        Test_case_2: Test that '__class__', 'id', 'created_at', 'updated_at',
        have the correct type
        """
        obj = BaseModel()
        modified_dict = obj.to_dict()
        reconstructed_obj = BaseModel(**(obj.to_dict()))
        reconstructed_modified_dict = reconstructed_obj.to_dict()
        # Test_case_1: new instance
        self.assertIsInstance(modified_dict, dict)
        self.assertTrue('__class__' in modified_dict)
        self.assertTrue('id' in modified_dict)
        self.assertTrue('created_at' in modified_dict)
        self.assertTrue('updated_at' in modified_dict)
        # Test_case_1: reconstructed instance
        self.assertIsInstance(reconstructed_modified_dict, dict)
        self.assertTrue('__class__' in reconstructed_modified_dict)
        self.assertTrue('id' in reconstructed_modified_dict)
        self.assertTrue('created_at' in reconstructed_modified_dict)
        self.assertTrue('updated_at' in reconstructed_modified_dict)

        # Test_case_2: new instance
        self.assertIsInstance(modified_dict['__class__'], str)
        self.assertIsInstance(modified_dict['id'], str)
        self.assertIsInstance(modified_dict['created_at'], str)
        self.assertIsInstance(modified_dict['updated_at'], str)
        # Test_case_2: reconstructed instance
        self.assertIsInstance(reconstructed_modified_dict['__class__'], str)
        self.assertIsInstance(reconstructed_modified_dict['id'], str)
        self.assertIsInstance(reconstructed_modified_dict['created_at'], str)
        self.assertIsInstance(reconstructed_modified_dict['updated_at'], str)

    def test_save(self):
        """
        The folowing test cases would check both:
            1.new instance
            2.and Reconstructed one
        Test that updated_at attribute changes upon invoking save
        """
        # Test_case_1: new instance
        obj = BaseModel()
        old_updated_atribute = obj.updated_at
        obj.save()
        new_updated_updated_at = obj.updated_at
        self.assertNotEqual(old_updated_atribute, new_updated_updated_at)
        # Test_case_1: reconstructed instance
        # Note: r at the beginning of a variable stands for : reconstructed
        reconstructed_obj = BaseModel(**(obj.to_dict()))
        r_old_updated_atribute = reconstructed_obj.updated_at
        reconstructed_obj.save()
        r_new_updated_updated_at = reconstructed_obj.updated_at
        self.assertNotEqual(r_old_updated_atribute, r_new_updated_updated_at)

    def test_str(self):
        """
        The folowing test cases would check both:
            1.new instance
            2.and Reconstructed one
        Test the return formatof  __str__ method
        """
        # Test_case_1: new instance
        obj = BaseModel()
        expected_return_format = (
            f"[{obj.__class__.__name__}] "
            f"({obj.id}) {obj.__dict__}"
            )
        self.assertEqual(obj.__str__(), expected_return_format)
        # Test_case_1: reconstructed instance
        reconstructed_obj = BaseModel(**(obj.to_dict()))
        r_expected_return_format = (
            f"[{reconstructed_obj.__class__.__name__}] "
            f"({reconstructed_obj.id}) {reconstructed_obj.__dict__}"
            )
        self.assertEqual(reconstructed_obj.__str__(), r_expected_return_format)


if __name__ == '__main__':
    unittest.main()
