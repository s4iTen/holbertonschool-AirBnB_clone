#!/usr/bin/pytohn3
"""this is the declaration of the class Review"""
from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    place_id = ""
    user_id = ""
    text = ""
