#!/usr/bin/python3
"""
Console module that contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """
    our command interpreter class that will implement
    quit, EOF, help, and a custom prompt (hbnb). An empty line + ENTER
    must not do anything
    """
    prompt = '(hbnb) '
    classes_list = ["BaseModel", "User", "State", "City", "Amenity", "Place",
                    "Review"]
    int_attrs = ["number_rooms", "number_bathrooms", "max_guest",
                 "price_by_night"]
    float_attrs = ["latitude", "longitude"]
    
    def do_EOF(self, line):
        """Quits console when CTRL + D is pressed"""
        print()
        return True
    
    def do_quit(self, line):
        """Quit command to exit the program"""
        return True
    
    def emptyline(self):
        """Empty line + ENTER must not execute anything"""
        pass

    
    if __name__ == '__main__':
    HBNBCommand().cmdloop()
