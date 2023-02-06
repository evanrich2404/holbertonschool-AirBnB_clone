#!/usr/bin/python3
""" this is the module for the class called BaseModel"""
import uuid
from datetime import datetime


class BaseModel:
    """this is the superclass for the airbnb project"""
    
    def __init__(self):
        """initializes the object function"""
        self.id = str(uuid.uuid4())
        