#!/usr/bin/python3
"""base model/module"""
from uuid import uuid
from datetime import datetime
import models



class BaseModel:
    """Base class for all other classes"""
    def __init__(self, *args, **kwargs):
        """Initialize an instance of BaseModel"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.datetime.strptime(value,
                                                       "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.datetime.now()
            models.storage.new(self)
    
    def __str__(self):
        """
        Returns a string representation of the instance
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def save(self):
        """
        Updates the public instance attribute updated_at with the current
        datetime
        """
        self.updated_at = datetime.datetime.now()
        models.storage.save()
    
    def to_dict(self):
        """Return a dictionary containing all keys/values of __dict__"""
        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if isinstance(value, datetime):
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value
        return new_dict
    