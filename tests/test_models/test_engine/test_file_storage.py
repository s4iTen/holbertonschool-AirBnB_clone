#!/usr/bin/python3
"""Unittest for FileStorage class"""

import os
import unittest
import json
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
        # Create a test JSON file with a single BaseModel instance
        test_dict = {"BaseModel.1234": {"id": "1234", "created_at": "2022-02-21T14:10:00.000000", "updated_at": "2022-02-21T14:10:00.000000", "__class__": "BaseModel"}}
        with open(FileStorage._FileStorage__file_path, "w") as f:
            json.dump(test_dict, f)

        # Create a FileStorage instance and call reload
        fs = FileStorage()
        fs.reload()

        # Check that the reloaded object matches the original object
        loaded_obj = fs.all()["BaseModel.1234"]
        self.assertIsInstance(loaded_obj, BaseModel)
        self.assertEqual(loaded_obj.id, "1234")
        self.assertEqual(str(loaded_obj.created_at), "2022-02-21 14:10:00")
        self.assertEqual(str(loaded_obj.updated_at), "2022-02-21 14:10:00")

        # Cleanup by deleting the test JSON file
        import os
        os.remove(FileStorage._FileStorage__file_path)


if __name__ == '__main__':
    unittest.main()