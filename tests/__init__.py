#!/usr/bin/python3
"""
this module is the unittest module for the BaseModel class
"""
from genericpath import exists
import unittest
from models.base_model import BaseModel
import pep8


class TestCaseModelClass(unitest.TestCase())
    """
    This class is for testing BaseModel.
    """
    def setUp(self):
        """
        Setup method.
        """
        self.User1 = BaseModel()
        self.User2 = BaseModel()

def test_str(self):
        """
        Testing __str__.
        """
        expected_display = "[{}] ({}) {}".format(
                self.User1.__class__.__name__,
                self.User1.id,
                self.User1.__dict__)
        self.assertEqual(self.User1.__str__(), expected_display)

    def test_save(self):
        """
        Testing save.
        """
        self.User1.save()
        self.assertNotEqual(self.User1.created_at, self.User1.updated_at)

    def test_to_dict(self):
        """
        Testing to_dict.
        """
        User1_dict = self.User1.to_dict()
        self.assertEqual(User1_dict['__class__'], 'BaseModel')
        self.assertEqual(User1_dict['created_at'],
                         self.User1.created_at.isoformat())
        self.assertEqual(User1_dict['updated_at'],
                         self.User1.updated_at.isoformat())
        self.assertEqual(User1_dict['id'], self.User1.id)

if __name__ == "__main__":
    unittest.main()
