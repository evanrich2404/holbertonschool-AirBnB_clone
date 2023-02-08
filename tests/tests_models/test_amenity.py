#!/usr/bin/python3
"""Amenity test module"""
import unittest
import models
import os
from datetime import datetime
from models.amenity import Amenity



class TestAmenityModel(unittest.TestCase):
    """Amenity test class"""
    def test_init(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_name_public(self):
        hottub = Amenity()
        self.assertEqual(str, type(Amenity.name))
        self.assertIn("name", dir(Amenity()))
        self.assertNotIn("name", hottub.__dict__)



if __name__ == "__main__":
    unittest.main()
