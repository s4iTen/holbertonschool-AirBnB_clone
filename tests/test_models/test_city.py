#!/usr/bin/python3
"""Unittest for City class"""
import unittest
import models
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for City"""
    def test_instance(self):
        """Test City instance"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_attributes(self):
        """Test City attributes"""
        city = City()
        self.assertTrue(hasattr(city, "state_id"))
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
