#!/usr/bin/python3
"""This is the main class BaseModel"""
import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        """this is the main Module"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        
    def __str__(self):
        """this Method change the print function"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = self.created_at

    def to_dict(self):
        """this Method return a dictionary containing all key/value
         of __dict__ of the instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
