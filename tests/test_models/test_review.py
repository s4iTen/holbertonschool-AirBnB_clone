#!/usr/bin/python3
"""
    Unittest for Review class.
"""
import unittest
import datetime
from models.review import Review


class TestReview(unittest.TestCase):
    """Defines the TestReview class."""

    def test_Review_instantiation(self):
        """Tests instantiation of Review class."""
        r = Review()
        self.assertIsInstance(r, Review)

    def test_Review_id(self):
        """Tests that each Review has a unique id."""
        r1 = Review()
        r2 = Review()
        self.assertNotEqual(r1.id, r2.id)

    def test_Review_attributes(self):
        """Tests that Review has expected attributes."""
        r = Review()
        self.assertTrue(hasattr(r, "place_id"))
        self.assertEqual(r.place_id, "")
        self.assertTrue(hasattr(r, "user_id"))
        self.assertEqual(r.user_id, "")
        self.assertTrue(hasattr(r, "text"))
        self.assertEqual(r.text, "")

    def test_Review_str(self):
        """Tests the __str__ method of Review."""
        r = Review()
        r_str = r.__str__()
        self.assertEqual(r_str, "[Review] ({}) {}".format(r.id, r.__dict__))

    def test_Review_updated_at(self):
        """Tests that Review has updated_at attribute."""
        r = Review()
        self.assertTrue(hasattr(r, "updated_at"))
        self.assertIsInstance(r.updated_at, datetime.datetime)

    def test_Review_created_at(self):
        """Tests that Review has created_at attribute."""
        r = Review()
        self.assertTrue(hasattr(r, "created_at"))
        self.assertIsInstance(r.created_at, datetime.datetime)

    def test_Review_to_dict(self):
        """Tests the to_dict method of Review."""
        r = Review()
        r_dict = r.to_dict()
        self.assertIsInstance(r_dict, dict)
        for key, value in r_dict.items():
            self.assertTrue(hasattr(r, key))
            if key == "created_at" or key == "updated_at":
                self.assertEqual(datetime.datetime.strptime(value,
                                                             "%Y-%m-%dT%H:%M:%S.%f"),
                                 getattr(r, key))
            else:
                self.assertEqual(str(value), str(getattr(r, key)))
