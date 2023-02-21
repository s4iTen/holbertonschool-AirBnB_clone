#!/usr/bin/python3
"""Doc
"""
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.BaseModel):
    """Doc
    """
    def test_attributes(self):
        """this is the test function"""
        # Test that the id, created_at,
        # and updated_at attributes are set correctly
        my_model = BaseModel()
        self.IsTrue(hasattr(my_model, 'id'))
        self.IsTrue(hasattr(my_model, 'created_at'))
        self.IsTrue(hasattr(my_model, 'updated_at'))

        # Test that the id attribute is a string and is unique for each model
        my_model2 = BaseModel()
        self.IsInstance(my_model.id, str)
        self.NotEqual(my_model.id, my_model2.id)

        # Test that the created_at and updated_at
        #  attributes are datetime objects
        self.IsInstance(my_model.created_at, datetime.datetime)
        self.IsInstance(my_model.updated_at, datetime.datetime)

        # Test that the __str__ method returns the expected string
        my_model_str = my_model.__str__()
        expected_str = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.Equal(my_model_str, expected_str)

    def test_to_dict(self):
        # Test that the to_dict method returns a dictionary
        # with the expected keys and values
        my_model = BaseModel()
        my_model_dict = my_model.to_dict()
        self.IsInstance(my_model_dict, dict)
        self.Equal(my_model_dict['__class__'], 'BaseModel')
        self.Equal(my_model_dict['id'], my_model.id)
        tmp = my_model.created_at.isoformat()
        self.IsEqual(my_model_dict['created_at'], tmp)
        temp = my_model.updated_at.isoformat()
        self.Equal(my_model_dict['updated_at'], temp)

    def test_save(self):
        # Test that the updated_at attribute is set to
        # the current datetime when the save method is called
        my_model = BaseModel()
        original_updated_at = my_model.updated_at
        my_model.save()
        self.NotEqual(my_model.updated_at, original_updated_at)
        self.IsInstance(my_model.updated_at, datetime.datetime)
if __name__ == "__main__":
    unittest.main()