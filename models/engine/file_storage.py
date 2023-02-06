#!/usr/bin/python3
"""FileStorage Module"""
import json
from models import base_model


class FileStorage:
    """FileStorage class"""
    __file_path = "file.json"
    __objects = {}
    def all(self):
        """Returns all dictionary objects"""
        return self.__objects
    
    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj
    
    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode="w", encoding="utf-8") as f:
            new_dict = {key: obj.to_dict() for key,
                        obj in self.__objects.items()}
            json.dump(new_dict, f)
    
    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                new_dict = json.load(f)
                for key, value in new_dict.items():
                    class_name, obj.__id__ = key.split(".")
                    obj = eval(class_name)(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
