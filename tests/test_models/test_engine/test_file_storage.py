#!/usr/bin/python3
"""Unittest for FileStorage class"""

import os
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down test environment"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test all method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test new method"""
        model = BaseModel()
        self.storage.new(model)
        key = "{}.{}".format(type(model).__name__, model.id)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test save method"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        with open("file.json", "r") as f:
            data = f.read()
        self.assertIn(type(model).__name__, data)
        self.assertIn(model.id, data)

    def test_reload(self):
        """Test reload method"""
        model = BaseModel()
        key = "{}.{}".format(type(model).__name__, model.id)
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        self.assertIn(key, self.storage.all())


if __name__ == '__main__':
    unittest.main()