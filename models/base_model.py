#!/usr/bin/python3
<<<<<<< HEAD

import models
from uuid import uuid4
from datetime import datetime
=======
from uuid import uuid4
from json import dumps
>>>>>>> c3ab1127958e4ddde59d04994f32256294523fa0


class BaseModel:

<<<<<<< HEAD
    def __init__(self, *args, **kwargs):
        timeformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for key, val in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(val, timeformat)
                else:
                    self.__dict__[key] = val
        else:
            models.storage.new(self)

    def save(self):
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        rt_dict = self.__dict__.copy()
        rt_dict["created_at"] = self.created_at.isoformat()
        rt_dict["updated_at"] = self.updated_at.isoformat()
        rt_dict["__class__"] = self.__class__.__name__
        return rt_dict

    def __str__(self):
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
=======
    def __init__(self):
        """Initialize instances
        of basemodel class"""
        self.id = str(uuid4())
        self.created_at
>>>>>>> c3ab1127958e4ddde59d04994f32256294523fa0
