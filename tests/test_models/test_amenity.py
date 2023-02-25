#!/usr/bin/python3
"""Unittest for Amenity class"""
import unittest
import models
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity"""
    def test_instance(self):
        """Test Amenity instance"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, "")

    def test_attributes(self):
        """Test Amenity attributes"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")
