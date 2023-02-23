#!/usr/bin/python3
"""Unittest for User"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for User class"""

    def test_instance_creation(self):
        """Test instance creation and type"""
        new_user = User()
        self.assertIsInstance(new_user, User)

    def test_attributes(self):
        """Test User attributes"""
        new_user = User()
        self.assertTrue(hasattr(new_user, "email"))
        self.assertTrue(hasattr(new_user, "password"))
        self.assertTrue(hasattr(new_user, "first_name"))
        self.assertTrue(hasattr(new_user, "last_name"))
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")

    def test_str_method(self):
        """Test User __str__ method"""
        new_user = User()
        expected = "[User] ({}) {}".format(new_user.id, new_user.__dict__)
        self.assertEqual(str(new_user), expected)

    def test_to_dict_method(self):
        """Test User to_dict method"""
        new_user = User()
        user_dict = new_user.to_dict()
        self.assertIsInstance(user_dict, dict)
        for attr in new_user.__dict__:
            self.assertIn(attr, user_dict)
            self.assertEqual(user_dict[attr], getattr(new_user, attr))

    def test_init_with_kwargs(self):
        """Test User init with kwargs"""
        kwargs = {
            "id": "1234",
            "email": "test@test.com",
            "password": "testpassword",
            "first_name": "John",
            "last_name": "Doe",
        }
        new_user = User(**kwargs)
        for key, value in kwargs.items():
            self.assertEqual(value, getattr(new_user, key))
        self.assertIsInstance(new_user, User)
        self.assertEqual(type(new_user.created_at).__name__, "datetime")
        self.assertEqual(type(new_user.updated_at).__name__, "datetime")
        self.assertTrue(hasattr(new_user, "id"))

if __name__ == '__main__':
    unittest.main()