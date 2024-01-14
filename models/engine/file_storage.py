#!/usr/bin/python3
"""module to store objects"""
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """
    Class to serialize instance to a JSON file and deserializes JSON file to
    instances

    ...
    attributes

    file_path str
        path to the JSON file
    objects dict
        store all objects with id

    methods

    all()
        return the dictionary objects
    new(obj)
        set the obj in the objects dict with the object id
    save()
        serialize the objects dict to a JSON fileto the file_path
    reload()
        deserialize JSON file to dict objects if the file_path exists
        otherwise do nothing
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return the objects dictionary"""
        return FileStorage.__objects

    def new(self, obj):
        """sets obj id in the dictionary __objects"""
        obj_cls_name = obj.__class__.__name__
        self.__objects["{}.{}".format(obj_cls_name, obj.id)] = obj

    def save(self):
        """save objects to JSON file"""
        obj_dict = {}
        for obj_id in FileStorage.__objects.keys():
            obj_dict[obj_id] = FileStorage.__objects[obj_id].to_dict()

        with open(FileStorage.__file_path, 'w') as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as json_file:
                obj = json.load(json_file)
                for o in obj.values():
                    cls_name = o["__class__"]
                    self.new(eval(cls_name)(**o))
