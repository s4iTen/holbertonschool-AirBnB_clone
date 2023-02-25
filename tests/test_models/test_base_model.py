#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class
    """
    def test_new_instance(self):
        """
        Test creating a new instance of BaseModel
        """
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_id_generation(self):
        """
        Test that BaseModel generates unique IDs
        """
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_to_dict_method(self):
        """
        Test that the to_dict method returns a
        dictionary representation of the BaseModel instance
        """
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertEqual(model_dict["id"], model.id)
        dic_create = model_dict["created_at"]
        dic_update = model_dict["updated_at"]
        self.assertEqual(dic_create, model.created_at.isoformat())
        self.assertEqual(dic_update, model.updated_at.isoformat())
        self.assertEqual(model_dict["__class__"], "BaseModel")

    def test_str_method(self):
        """
        Test that the __str__ method returns a
        string representation of the BaseModel instance
        """
        model = BaseModel()
        model_str = str(model)
        self.assertIn("[BaseModel]", model_str)
        self.assertIn("'id': '{}'".format(model.id), model_str)
        self.assertIn("'created_at': {}".format(model.created_at), model_str)
        self.assertIn("'updated_at': {}".format(model.updated_at), model_str)
