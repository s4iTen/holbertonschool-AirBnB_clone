#!/usr/bin/python3
"""Unittest for State class"""
import unittest
import models
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for State"""
    def test_instance(self):
        """Test State instance"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, "")

    def test_attributes(self):
        """Test State attributes"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")
