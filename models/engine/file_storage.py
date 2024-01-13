#!/usr/bin/python3
"""Engine"""


import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key,
                    obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objs = json.load(f)
                for key, value in objs.items():
                    cls_name = value['__class__']
                    del value['__class__']
                    if cls_name == 'BaseModel':
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif cls_name == 'User':
                        FileStorage.__objects[key] = User(**value)
        except FileNotFoundError:
            pass
