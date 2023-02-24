#!/usr/bin/python3
"""this is the class City"""
from models.base_model import BaseModel
from models.state import State


class City(BaseModel):
    state_id = State.id
    name = ""
